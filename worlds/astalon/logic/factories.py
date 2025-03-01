import dataclasses
import operator
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Tuple, Union

from ..items import Character, Eye, KeyItem, ShopUpgrade
from ..options import Goal, RandomizeCharacters
from .instances import (
    AndInstance,
    CanReachEntranceInstance,
    CanReachLocationInstance,
    CanReachRegionInstance,
    FalseInstance,
    HasAllInstance,
    HasAnyInstance,
    HasInstance,
    NestedRuleInstance,
    OrInstance,
    TrueInstance,
)

if TYPE_CHECKING:
    from Options import CommonOptions, Option

    from ..items import BlueDoor, Crystal, Elevator, Face, ItemName, RedDoor, Switch, WhiteDoor
    from ..locations import LocationName
    from ..regions import RegionName
    from ..world import AstalonWorld
    from .instances import RuleInstance


ITEM_DEPS: "Dict[str, Tuple[Character, ...]]" = {
    KeyItem.CLOAK.value: (Character.ALGUS,),
    KeyItem.SWORD.value: (Character.ARIAS,),
    KeyItem.BOOTS.value: (Character.ARIAS,),
    KeyItem.CLAW.value: (Character.KYULI,),
    KeyItem.BOW.value: (Character.KYULI,),
    KeyItem.BLOCK.value: (Character.ZEEK,),
    KeyItem.STAR.value: (Character.BRAM,),
    KeyItem.BANISH.value: (Character.ALGUS, Character.ZEEK),
    KeyItem.GAUNTLET.value: (Character.ARIAS, Character.BRAM),
    ShopUpgrade.ALGUS_ARCANIST.value: (Character.ALGUS,),
    ShopUpgrade.ALGUS_METEOR.value: (Character.ALGUS,),
    ShopUpgrade.ALGUS_SHOCK.value: (Character.ALGUS,),
    ShopUpgrade.ARIAS_GORGONSLAYER.value: (Character.ARIAS,),
    ShopUpgrade.ARIAS_LAST_STAND.value: (Character.ARIAS,),
    ShopUpgrade.ARIAS_LIONHEART.value: (Character.ARIAS,),
    ShopUpgrade.KYULI_ASSASSIN.value: (Character.KYULI,),
    ShopUpgrade.KYULI_BULLSEYE.value: (Character.KYULI,),
    ShopUpgrade.KYULI_RAY.value: (Character.KYULI,),
    ShopUpgrade.ZEEK_JUNKYARD.value: (Character.ZEEK,),
    ShopUpgrade.ZEEK_ORBS.value: (Character.ZEEK,),
    ShopUpgrade.ZEEK_LOOT.value: (Character.ZEEK,),
    ShopUpgrade.BRAM_AXE.value: (Character.BRAM,),
    ShopUpgrade.BRAM_HUNTER.value: (Character.BRAM,),
    ShopUpgrade.BRAM_WHIPLASH.value: (Character.BRAM,),
}

VANILLA_CHARACTERS = frozenset((Character.ALGUS, Character.ARIAS, Character.KYULI))
OPERATORS = {
    "eq": operator.eq,
    "ne": operator.ne,
    "gt": operator.gt,
    "lt": operator.lt,
    "ge": operator.ge,
    "le": operator.le,
    "contains": operator.contains,
}

characters_off = ("randomize_characters", 0)
characters_on = ("randomize_characters__ge", 1)


@dataclasses.dataclass()
class RuleFactory:
    opts: Tuple[Tuple[str, Any], ...] = dataclasses.field(default=(), kw_only=True)

    instance_cls: "ClassVar[type[RuleInstance]]"

    def _pass_opts(self, options: "CommonOptions") -> bool:
        for key, value in self.opts:
            parts = key.split("__", maxsplit=1)
            option_name = parts[0]
            operator = parts[1] if len(parts) > 1 else "eq"
            opt: Option = getattr(options, option_name)
            if not OPERATORS[operator](opt.value, value):
                return False
        return True

    def _instantiate(self, world: "AstalonWorld") -> "RuleInstance":
        return self.instance_cls(player=world.player)

    def resolve(self, world: "AstalonWorld") -> "RuleInstance":
        if not self._pass_opts(world.options):
            return FalseInstance(player=world.player)
        return self._instantiate(world)

    def serialize(self) -> str:
        return f"{self.__class__.__name__}()"


@dataclasses.dataclass()
class True_(RuleFactory):
    instance_cls = TrueInstance

    def serialize(self) -> str:
        return "True"


@dataclasses.dataclass()
class False_(RuleFactory):
    instance_cls = FalseInstance

    def serialize(self) -> str:
        return "False"


@dataclasses.dataclass(init=False)
class NestedRuleFactory(RuleFactory):
    children: "Tuple[RuleFactory, ...]"

    instance_cls = NestedRuleInstance

    def _instantiate(self, world: "AstalonWorld") -> "RuleInstance":
        children = [c.resolve(world) for c in self.children]
        return self.instance_cls(tuple(children), player=world.player).simplify()  # type: ignore

    def __init__(self, *children: "RuleFactory", opts: Tuple[Tuple[str, Any], ...] = ()) -> None:
        super().__init__(opts=opts)
        self.children = children


@dataclasses.dataclass(init=False)
class And(NestedRuleFactory):
    instance_cls = AndInstance

    def serialize(self) -> str:
        return f"({' + '.join(child.serialize() for child in self.children)})"


@dataclasses.dataclass(init=False)
class Or(NestedRuleFactory):
    instance_cls = OrInstance

    def serialize(self) -> str:
        return f"({' | '.join(child.serialize() for child in self.children)})"


@dataclasses.dataclass()
class Has(RuleFactory):
    item: "ItemName"
    count: int = 1

    instance_cls = HasInstance

    def _instantiate(self, world: "AstalonWorld") -> "RuleInstance":
        default = HasInstance(self.item.value, self.count, player=world.player)

        if self.item in VANILLA_CHARACTERS:
            if world.options.randomize_characters == RandomizeCharacters.option_vanilla:
                return TrueInstance(player=world.player)
            return default

        if deps := ITEM_DEPS.get(self.item):
            if world.options.randomize_characters == RandomizeCharacters.option_vanilla and (
                len(deps) > 1 or (len(deps) == 1 and deps[0] in VANILLA_CHARACTERS)
            ):
                return default
            if len(deps) == 1:
                return HasAllInstance((deps[0].value, self.item.value), player=world.player)
            return OrInstance(
                tuple(HasAllInstance((d.value, self.item.value), player=world.player) for d in deps),
                player=world.player,
            )

        return default

    def serialize(self) -> str:
        return f"Has({self.item.value})"


@dataclasses.dataclass(init=False)
class HasAll(RuleFactory):
    items: "Tuple[ItemName, ...]"

    instance_cls = HasAllInstance

    def __init__(self, *items: "ItemName", opts: Tuple[Tuple[str, Any], ...] = ()) -> None:
        super().__init__(opts=opts)
        self.items = items

    def _instantiate(self, world: "AstalonWorld") -> "RuleInstance":
        if len(self.items) == 0:
            return TrueInstance(player=world.player)
        if len(self.items) == 1:
            return Has(self.items[0]).resolve(world)

        new_clauses: List[RuleInstance] = []
        new_items: List[str] = []
        for item in self.items:
            if (
                item in VANILLA_CHARACTERS
                and world.options.randomize_characters == RandomizeCharacters.option_vanilla
            ):
                continue
            deps = ITEM_DEPS.get(item, [])
            if not deps:
                new_items.append(item.value)
                continue

            if len(deps) > 1:
                if world.options.randomize_characters == RandomizeCharacters.option_vanilla:
                    new_items.append(item.value)
                else:
                    new_clauses.append(
                        OrInstance(
                            tuple(HasAllInstance((d.value, item.value), player=world.player) for d in deps),
                            player=world.player,
                        )
                    )
                continue

            if (
                len(deps) == 1
                and deps[0] not in self.items
                and not (
                    deps[0] in VANILLA_CHARACTERS
                    and world.options.randomize_characters == RandomizeCharacters.option_vanilla
                )
            ):
                new_items.append(deps[0].value)

            new_items.append(item.value)

        if len(new_clauses) == 0 and len(new_items) == 0:
            return TrueInstance(player=world.player)
        if len(new_items) == 1:
            new_clauses.append(HasInstance(new_items[0], player=world.player))
        elif len(new_items) > 1:
            new_clauses.append(HasAllInstance(tuple(new_items), player=world.player))
        if len(new_clauses) == 0:
            return FalseInstance(player=world.player)
        if len(new_clauses) == 1:
            return new_clauses[0]
        return AndInstance(tuple(new_clauses), player=world.player)

    def serialize(self) -> str:
        return f"HasAll({', '.join(i.value for i in self.items)})"


@dataclasses.dataclass(init=False)
class HasAny(RuleFactory):
    items: "Tuple[ItemName, ...]"

    instance_cls = HasAnyInstance

    def __init__(self, *items: "ItemName", opts: Tuple[Tuple[str, Any], ...] = ()) -> None:
        super().__init__(opts=opts)
        self.items = items

    def _instantiate(self, world: "AstalonWorld") -> "RuleInstance":
        if len(self.items) == 0:
            return TrueInstance(player=world.player)
        if len(self.items) == 1:
            return Has(self.items[0]).resolve(world)

        new_clauses: List[RuleInstance] = []
        new_items: List[str] = []
        for item in self.items:
            if (
                item in VANILLA_CHARACTERS
                and world.options.randomize_characters == RandomizeCharacters.option_vanilla
            ):
                return TrueInstance(player=world.player)

            deps = ITEM_DEPS.get(item, [])
            if not deps:
                new_items.append(item.value)
                continue

            if len(deps) > 1:
                if world.options.randomize_characters == RandomizeCharacters.option_vanilla:
                    new_items.append(item.value)
                else:
                    new_clauses.append(
                        OrInstance(
                            tuple(HasAllInstance((d.value, item.value), player=world.player) for d in deps),
                            player=world.player,
                        )
                    )
                continue

            if (
                len(deps) == 1
                and deps[0] not in self.items
                and not (
                    deps[0] in VANILLA_CHARACTERS
                    and world.options.randomize_characters == RandomizeCharacters.option_vanilla
                )
            ):
                new_clauses.append(HasAllInstance((deps[0].value, item.value), player=world.player))
            else:
                new_items.append(item.value)

        if len(new_items) == 1:
            new_clauses.append(HasInstance(new_items[0], player=world.player))
        elif len(new_items) > 1:
            new_clauses.append(HasAnyInstance(tuple(new_items), player=world.player))

        if len(new_clauses) == 0:
            return FalseInstance(player=world.player)
        if len(new_clauses) == 1:
            return new_clauses[0]
        return OrInstance(tuple(new_clauses), player=world.player)

    def serialize(self) -> str:
        return f"HasAny({', '.join(i.value for i in self.items)})"


@dataclasses.dataclass()
class CanReachLocation(RuleFactory):
    location: "LocationName"

    instance_cls = CanReachLocationInstance

    def _instantiate(self, world: "AstalonWorld") -> "RuleInstance":
        location = world.get_location(self.location.value)
        if not location.parent_region:
            raise ValueError(f"Location {location.name} has no parent region")
        return CanReachLocationInstance(location.name, location.parent_region.name, player=world.player)

    def serialize(self) -> str:
        return f"CanReachLocation({self.location.value})"


@dataclasses.dataclass()
class CanReachRegion(RuleFactory):
    region: "RegionName"

    instance_cls = CanReachRegionInstance

    def _instantiate(self, world: "AstalonWorld") -> "RuleInstance":
        return CanReachRegionInstance(self.region.value, player=world.player)

    def serialize(self) -> str:
        return f"CanReachRegion({self.region.value})"


@dataclasses.dataclass()
class CanReachEntrance(RuleFactory):
    from_region: "RegionName"
    to_region: "RegionName"

    instance_cls = CanReachEntranceInstance

    def _instantiate(self, world: "AstalonWorld") -> "RuleInstance":
        entrance = f"{self.from_region.value} -> {self.to_region.value}"
        return CanReachEntranceInstance(entrance, player=world.player)

    def serialize(self) -> str:
        return f"CanReachEntrance({self.from_region.value} -> {self.to_region.value})"


@dataclasses.dataclass(init=False)
class ToggleRule(HasAll):
    option_name: ClassVar[str]
    otherwise: bool = False

    def _instantiate(self, world: "AstalonWorld") -> "RuleInstance":
        if len(self.items) == 1:
            rule = Has(self.items[0], opts=((self.option_name, 1),))
        else:
            rule = HasAll(*self.items, opts=((self.option_name, 1),))

        if self.otherwise:
            return Or(
                rule,
                True_(opts=((self.option_name, 0),)),
            ).resolve(world)

        return rule.resolve(world)


@dataclasses.dataclass(init=False)
class HasWhite(ToggleRule):
    option_name = "randomize_white_keys"

    def __init__(
        self,
        *doors: "WhiteDoor",
        otherwise: bool = False,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(*doors, opts=opts)
        self.otherwise = otherwise


@dataclasses.dataclass(init=False)
class HasBlue(ToggleRule):
    option_name = "randomize_blue_keys"

    def __init__(
        self,
        *doors: "BlueDoor",
        otherwise: bool = False,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(*doors, opts=opts)
        self.otherwise = otherwise


@dataclasses.dataclass(init=False)
class HasRed(ToggleRule):
    option_name = "randomize_red_keys"

    def __init__(
        self,
        *doors: "RedDoor",
        otherwise: bool = False,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(*doors, opts=opts)
        self.otherwise = otherwise


@dataclasses.dataclass(init=False)
class HasSwitch(ToggleRule):
    option_name = "randomize_switches"

    def __init__(
        self,
        *switches: "Union[Switch, Crystal, Face]",
        otherwise: bool = False,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(*switches, opts=opts)
        self.otherwise = otherwise


@dataclasses.dataclass(init=False)
class HasElevator(HasAll):
    def __init__(self, elevator: "Elevator", *, opts: Tuple[Tuple[str, Any], ...] = ()) -> None:
        super().__init__(KeyItem.ASCENDANT_KEY, elevator, opts=(*opts, ("randomize_elevator", 1)))


@dataclasses.dataclass()
class HasGoal(RuleFactory):
    def _instantiate(self, world: "AstalonWorld") -> "RuleInstance":
        if world.options.goal != Goal.option_eye_hunt:
            return TrueInstance(player=world.player)
        return HasInstance(Eye.GOLD.value, count=world.required_gold_eyes, player=world.player)
