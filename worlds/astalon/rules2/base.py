import dataclasses
import itertools
from copy import copy
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Set, Tuple, Union

from typing_extensions import Self

from BaseClasses import CollectionState

from ..items import Character, Eye, KeyItem, ShopUpgrade
from ..options import Goal, RandomizeCharacters
from ..regions import RegionName

if TYPE_CHECKING:
    from BaseClasses import CollectionState
    from Options import CommonOptions, Option

    from ..items import BlueDoor, Crystal, Elevator, Face, ItemName, RedDoor, Switch, WhiteDoor
    from ..locations import LocationName
    from ..world import AstalonWorld


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

characters_off = ("randomize_characters", 0)
characters_on = ("randomize_characters__gte", 1)


@dataclasses.dataclass()
class Rule:
    _: dataclasses.KW_ONLY
    result: bool = dataclasses.field(default=False, repr=False, init=False)
    player: int = -1
    opts: Tuple[Tuple[str, Any], ...] = ()
    cacheable: bool = dataclasses.field(
        default=False, repr=False, init=False
    )  # TODO: fix caching and reenable

    truthy: ClassVar = False
    falsy: ClassVar = False

    def _evaluate(self, state: "CollectionState") -> bool: ...

    def _pass_opts(self, options: "CommonOptions") -> bool:
        for key, value in self.opts:
            parts = key.split("__", maxsplit=1)
            option_name = parts[0]
            operator = parts[1] if len(parts) > 1 else "eq"
            opt: Option = getattr(options, option_name)
            if operator == "eq" and opt.value != value:
                return False
            if operator == "ne" and opt.value == value:
                return False
            if operator == "gt" and opt.value <= value:
                return False
            if operator == "gte" and opt.value < value:
                return False
            if operator == "lt" and opt.value >= value:
                return False
            if operator == "lte" and opt.value > value:
                return False
        return True

    def evaluate(self, state: "CollectionState") -> None:
        self.result = self._evaluate(state)
        state._astalon_computed_rules[self.player].add(id(self))  # type: ignore

    def stale(self, state: "CollectionState") -> bool:
        return not self.cacheable or id(self) not in state._astalon_computed_rules[self.player]  # type: ignore

    def test(self, state) -> bool:
        if self.stale(state):
            self.evaluate(state)
        return self.result

    def clone(self, world: "AstalonWorld") -> Self:
        new_rule = copy(self)
        new_rule.player = world.player
        new_rule.opts = ()
        return new_rule

    def actualize(self, world: "AstalonWorld") -> "Rule":
        if self.player > -1:
            return self
        if not self._pass_opts(world.options):
            return False_(player=world.player)
        return self.clone(world)

    def deps(self) -> "Dict[str, Set[int]]":
        return {}

    def indirect(self) -> "Tuple[RegionName, ...]":
        return ()

    def serialize(self) -> str:
        return f"{self.__class__.__name__}()"


@dataclasses.dataclass()
class True_(Rule):
    truthy = True

    def _evaluate(self, state: "CollectionState") -> bool:
        return True


@dataclasses.dataclass()
class False_(Rule):
    falsy = True

    def _evaluate(self, state: "CollectionState") -> bool:
        return False


@dataclasses.dataclass(init=False)
class NestedRule(Rule):
    children: "Tuple[Rule, ...]"

    def __init__(self, *children: "Rule", player: int = -1, opts: Tuple[Tuple[str, Any], ...] = ()) -> None:
        super().__init__(player=player, opts=opts)
        self.children = children

    def deps(self) -> "Dict[str, Set[int]]":
        combined_deps: Dict[str, Set[int]] = {}
        for child in self.children:
            for item_name, rules in child.deps().items():
                if item_name in combined_deps:
                    combined_deps[item_name] |= rules
                else:
                    combined_deps[item_name] = {id(self), *rules}
        return combined_deps

    def indirect(self) -> "Tuple[RegionName, ...]":
        return tuple(itertools.chain.from_iterable(child.indirect() for child in self.children))


@dataclasses.dataclass(init=False)
class And(NestedRule):
    def _evaluate(self, state: "CollectionState") -> bool:
        for rule in self.children:
            if not rule.test(state):
                return False
        return True

    def actualize(self, world: "AstalonWorld") -> "Rule":
        if self.player > -1:
            return self
        if not self._pass_opts(world.options):
            return False_(player=world.player)

        true_rule: Union[Rule, None] = None
        new_children: List[Rule] = []
        all_items: List[str] = []
        only_has = True
        for child in self.children:
            new_child = child.actualize(world)
            if new_child is None:
                continue
            if new_child.falsy:
                # false always wins
                return new_child
            if new_child.truthy:
                # dedupe trues
                true_rule = new_child
                continue
            if isinstance(new_child, Has):
                if new_child.count == 1:
                    all_items.append(new_child.item)
                else:
                    only_has = False
            elif isinstance(new_child, HasAll):
                all_items.extend(new_child.items)
            else:
                only_has = False
            new_children.append(new_child)

        # TODO: unnest nested ands
        if not new_children:
            return true_rule or False_(player=world.player)
        if only_has:
            if len(all_items) == 1:
                return Has(all_items[0], player=world.player)
            return HasAll(*all_items, player=world.player)
        if len(new_children) == 1:
            return new_children[0]

        new_rule = self.clone(world)
        new_rule.children = tuple(new_children)
        new_rule.cacheable = all(child.cacheable for child in new_children)
        return new_rule

    def serialize(self) -> str:
        return f"({' + '.join(child.serialize() for child in self.children)})"


@dataclasses.dataclass(init=False)
class Or(NestedRule):
    def _evaluate(self, state: "CollectionState") -> bool:
        for rule in self.children:
            if rule.test(state):
                return True
        return False

    def actualize(self, world: "AstalonWorld") -> "Rule":
        if self.player > -1:
            return self
        if not self._pass_opts(world.options):
            return False_(player=world.player)

        new_children: List[Rule] = []
        all_items: List[str] = []
        only_has = True
        for child in self.children:
            new_child = child.actualize(world)
            if new_child is None:
                continue
            if new_child.truthy:
                # true always wins
                return new_child
            if new_child.falsy:
                # falses can be ignored
                continue
            if isinstance(new_child, Has):
                if new_child.count == 1:
                    all_items.append(new_child.item)
                else:
                    only_has = False
            elif isinstance(new_child, HasAny):
                all_items.extend(new_child.items)
            else:
                only_has = False
            new_children.append(new_child)

        if not new_children:
            return False_(player=world.player)
        if only_has:
            if len(all_items) == 1:
                return Has(all_items[0], player=world.player)
            return HasAny(*all_items, player=world.player)
        if len(new_children) == 1:
            return new_children[0]

        new_rule = self.clone(world)
        new_rule.children = tuple(new_children)
        new_rule.cacheable = all(child.cacheable for child in new_children)
        return new_rule

    def serialize(self) -> str:
        return f"({' | '.join(child.serialize() for child in self.children)})"


@dataclasses.dataclass(init=False)
class Has(Rule):
    item: str
    count: int

    def __init__(
        self,
        item: "Union[ItemName, str]",
        count: int = 1,
        *,
        player: int = -1,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(player=player, opts=opts)
        self.item = item.value if isinstance(item, Enum) else item
        self.count = count

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.has(self.item, self.player, count=self.count)

    def actualize(self, world: "AstalonWorld") -> "Rule":
        if self.player > -1:
            return self
        if not self._pass_opts(world.options):
            return False_(player=world.player)

        if self.item in VANILLA_CHARACTERS:
            if world.options.randomize_characters == RandomizeCharacters.option_vanilla:
                return True_(player=world.player)
            return self.clone(world)

        if deps := ITEM_DEPS.get(self.item):
            if world.options.randomize_characters == RandomizeCharacters.option_vanilla and (
                len(deps) > 1 or (len(deps) == 1 and deps[0] in VANILLA_CHARACTERS)
            ):
                return self.clone(world)
            return Or(*[HasAll(d, self.item) for d in deps]).actualize(world)

        return self.clone(world)

    def deps(self) -> Dict[str, Set[int]]:
        return {self.item: {id(self)}}

    def serialize(self) -> str:
        return f"Has({self.item})"


@dataclasses.dataclass(init=False)
class HasAll(Rule):
    items: Tuple[str, ...]

    def __init__(
        self,
        *items: "Union[ItemName, str]",
        player: int = -1,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(player=player, opts=opts)
        self.items = tuple(item.value if isinstance(item, Enum) else item for item in items)

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.has_all(self.items, self.player)

    def actualize(self, world: "AstalonWorld") -> "Rule":
        if self.player > -1:
            return self
        if not self._pass_opts(world.options):
            return False_(player=world.player)

        if len(self.items) == 0:
            return True_(player=world.player)
        if len(self.items) == 1:
            return Has(self.items[0]).actualize(world)

        new_clauses: List[Rule] = []
        new_items: List[str] = []
        for item in self.items:
            if (
                item in VANILLA_CHARACTERS
                and world.options.randomize_characters == RandomizeCharacters.option_vanilla
            ):
                continue
            deps = ITEM_DEPS.get(item, [])
            if not deps:
                new_items.append(item)
                continue

            if len(deps) > 1:
                if world.options.randomize_characters == RandomizeCharacters.option_vanilla:
                    new_items.append(item)
                else:
                    new_clauses.append(
                        Or(*[HasAll(d, item, player=world.player) for d in deps], player=world.player)
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
                new_items.append(deps[0])

            new_items.append(item)

        if len(new_clauses) == 0 and len(new_items) == 0:
            return True_(player=world.player)
        if len(new_items) == 1:
            new_clauses.append(Has(new_items[0], player=world.player))
        elif len(new_items) > 1:
            new_clauses.append(HasAll(*new_items, player=world.player))
        return And(*new_clauses).actualize(world)

    def deps(self) -> Dict[str, Set[int]]:
        return {item: {id(self)} for item in self.items}

    def serialize(self) -> str:
        return f"HasAll({', '.join(self.items)})"


@dataclasses.dataclass(init=False)
class HasAny(Rule):
    items: Tuple[str, ...]

    def __init__(
        self,
        *items: "Union[ItemName, str]",
        player: int = -1,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(player=player, opts=opts)
        self.items = tuple(item.value if isinstance(item, Enum) else item for item in items)

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.has_any(self.items, self.player)

    def actualize(self, world: "AstalonWorld") -> "Rule":
        if self.player > -1:
            return self
        if not self._pass_opts(world.options):
            return False_(player=world.player)

        if len(self.items) == 0:
            return True_(player=world.player)
        if len(self.items) == 1:
            return Has(self.items[0]).actualize(world)

        new_clauses: List[Rule] = []
        new_items: List[str] = []
        for item in self.items:
            if (
                item in VANILLA_CHARACTERS
                and world.options.randomize_characters == RandomizeCharacters.option_vanilla
            ):
                return True_(player=world.player)

            deps = ITEM_DEPS.get(item, [])
            if not deps:
                new_items.append(item)
                continue

            if len(deps) > 1:
                if world.options.randomize_characters == RandomizeCharacters.option_vanilla:
                    new_items.append(item)
                else:
                    new_clauses.append(
                        Or(*[HasAll(d, item, player=world.player) for d in deps], player=world.player)
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
                new_clauses.append(HasAll(deps[0], item, player=world.player))
            else:
                new_items.append(item)

        if len(new_items) == 1:
            new_clauses.append(Has(new_items[0], player=world.player))
        elif len(new_items) > 1:
            new_clauses.append(HasAny(*new_items, player=world.player))
        return Or(*new_clauses).actualize(world)

    def deps(self) -> Dict[str, Set[int]]:
        return {item: {id(self)} for item in self.items}

    def serialize(self) -> str:
        return f"HasAny({', '.join(self.items)})"


@dataclasses.dataclass(init=False)
class CanReachLocation(Rule):
    location: str

    def __init__(
        self,
        location: "Union[LocationName, str]",
        *,
        player: int = -1,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(player=player, opts=opts)
        self.location = location.value if isinstance(location, Enum) else location
        self.cacheable = False

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.can_reach_location(self.location, self.player)

    def serialize(self) -> str:
        return f"CanReachLocation({self.location})"


@dataclasses.dataclass(init=False)
class CanReachRegion(Rule):
    region: str

    def __init__(
        self,
        region: "Union[RegionName, str]",
        *,
        player: int = -1,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(player=player, opts=opts)
        self.region = region.value if isinstance(region, Enum) else region
        self.cacheable = False

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.can_reach_region(self.region, self.player)

    def indirect(self) -> "Tuple[RegionName, ...]":
        return (RegionName(self.region),)

    def serialize(self) -> str:
        return f"CanReachLocation({self.region})"


@dataclasses.dataclass(init=False)
class CanReachEntrance(Rule):
    entrance: str

    def __init__(
        self,
        from_region: "Union[RegionName, str]",
        to_region: "Union[RegionName, str]",
        *,
        player: int = -1,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(player=player, opts=opts)
        from_region = from_region.value if isinstance(from_region, Enum) else from_region
        to_region = to_region.value if isinstance(to_region, Enum) else to_region
        self.entrance = f"{from_region} -> {to_region}"
        self.cacheable = False

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.can_reach_entrance(self.entrance, self.player)

    def serialize(self) -> str:
        return f"CanReachLocation({self.entrance})"


@dataclasses.dataclass(init=False)
class ToggleRule(HasAll):
    option_name: ClassVar[str]
    otherwise: bool = False

    def actualize(self, world: "AstalonWorld") -> "Rule":
        if not self._pass_opts(world.options):
            return False_(player=world.player)

        if len(self.items) == 1:
            rule = Has(self.items[0], opts=((self.option_name, 1),))
        else:
            rule = HasAll(*self.items, opts=((self.option_name, 1),))

        if self.otherwise:
            return Or(
                rule,
                True_(opts=((self.option_name, 0),)),
            ).actualize(world)

        return rule.actualize(world)


@dataclasses.dataclass(init=False)
class HasWhite(ToggleRule):
    option_name = "randomize_white_keys"

    def __init__(
        self,
        *doors: "WhiteDoor",
        otherwise=False,
        player: int = -1,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(*doors, player=player, opts=opts)
        self.otherwise = otherwise


@dataclasses.dataclass(init=False)
class HasBlue(ToggleRule):
    option_name = "randomize_blue_keys"

    def __init__(
        self,
        *doors: "BlueDoor",
        otherwise=False,
        player: int = -1,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(*doors, player=player, opts=opts)
        self.otherwise = otherwise


@dataclasses.dataclass(init=False)
class HasRed(ToggleRule):
    option_name = "randomize_red_keys"

    def __init__(
        self,
        *doors: "RedDoor",
        otherwise=False,
        player: int = -1,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(*doors, player=player, opts=opts)
        self.otherwise = otherwise


@dataclasses.dataclass(init=False)
class HasSwitch(ToggleRule):
    option_name = "randomize_switches"

    def __init__(
        self,
        *switches: "Union[Switch, Crystal, Face]",
        otherwise=False,
        player: int = -1,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(*switches, player=player, opts=opts)
        self.otherwise = otherwise


@dataclasses.dataclass(init=False)
class HasElevator(HasAll):
    def __init__(
        self,
        elevator: "Elevator",
        *,
        player: int = -1,
        opts: Tuple[Tuple[str, Any], ...] = (),
    ) -> None:
        super().__init__(
            KeyItem.ASCENDANT_KEY,
            elevator,
            player=player,
            opts=(*opts, ("randomize_elevator", 1)),
        )


@dataclasses.dataclass()
class HasGoal(Rule):
    def actualize(self, world: "AstalonWorld") -> "Rule":
        if not self._pass_opts(world.options):
            return False_(player=world.player)

        if world.options.goal != Goal.option_eye_hunt:
            return True_(player=world.player)
        return Has(Eye.GOLD, count=world.required_gold_eyes, player=world.player)
