import dataclasses
from typing import TYPE_CHECKING, Any, ClassVar

from typing_extensions import override

import rule_builder

from ..items import (
    BlueDoor,
    Character,
    Crystal,
    Elevator,
    Events,
    Eye,
    Face,
    ItemName,
    KeyItem,
    RedDoor,
    ShopUpgrade,
    Switch,
    WhiteDoor,
)
from ..options import (
    Difficulty,
    Goal,
    RandomizeBlueKeys,
    RandomizeCharacters,
    RandomizeElevator,
    RandomizeRedKeys,
    RandomizeSwitches,
    RandomizeWhiteKeys,
)
from ..world import AstalonWorld

if TYPE_CHECKING:
    from collections.abc import Iterable

    from BaseClasses import CollectionState
    from NetUtils import JSONMessagePart
    from Options import Option

    from ..locations import LocationName
    from ..regions import RegionName


ITEM_DEPS: "dict[str, tuple[Character, ...]]" = {
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

VANILLA_CHARACTERS: "frozenset[Character]" = frozenset((Character.ALGUS, Character.ARIAS, Character.KYULI))

characters_off = [rule_builder.OptionFilter(RandomizeCharacters, RandomizeCharacters.option_vanilla)]
characters_on = [rule_builder.OptionFilter(RandomizeCharacters, RandomizeCharacters.option_vanilla, operator="gt")]


def _printjson_item(item: str, player: int, state: "CollectionState | None" = None) -> "JSONMessagePart":
    message: JSONMessagePart = {"type": "item_name", "flags": 0b001, "text": item, "player": player}
    if state:
        color = "green" if state.has(item, player) else "salmon"
        if item == Events.FAKE_OOL_ITEM:
            color = "glitched"
        message["color"] = color
    return message


@rule_builder.custom_rule(AstalonWorld)
class Has(rule_builder.Rule[AstalonWorld]):
    item_name: "ItemName | Events"
    count: int = 1

    @override
    def _instantiate(self, world: "AstalonWorld") -> "rule_builder.Rule.Resolved":
        default = self.Resolved(self.item_name.value, self.count, player=world.player)

        if self.item_name in VANILLA_CHARACTERS:
            if world.options.randomize_characters.value == RandomizeCharacters.option_vanilla:
                return rule_builder.True_.Resolved(player=world.player)
            return default

        if deps := ITEM_DEPS.get(self.item_name):
            if world.options.randomize_characters.value == RandomizeCharacters.option_vanilla and (
                len(deps) > 1 or (len(deps) == 1 and deps[0] in VANILLA_CHARACTERS)
            ):
                return default
            if len(deps) == 1:
                return HasAll.Resolved((deps[0].value, self.item_name.value), player=world.player)
            return rule_builder.Or.Resolved(
                tuple(HasAll.Resolved((d.value, self.item_name.value), player=world.player) for d in deps),
                player=world.player,
            )

        return default

    @override
    def __str__(self) -> str:
        count = f", count={self.count}" if self.count > 1 else ""
        options = f", options={self.options}" if self.options else ""
        return f"{self.__class__.__name__}({self.item_name.value}{count}{options})"

    @dataclasses.dataclass(frozen=True)
    class Resolved(rule_builder.Has.Resolved):
        @override
        def explain_json(self, state: "CollectionState | None" = None) -> "list[JSONMessagePart]":
            messages = super().explain_json(state)
            messages[-1] = _printjson_item(self.item_name, self.player, state)
            return messages


@rule_builder.custom_rule(AstalonWorld)
class HasAll(rule_builder.Rule[AstalonWorld]):
    item_names: "tuple[ItemName | Events, ...]"

    def __init__(
        self,
        *item_names: "ItemName | Events",
        options: "Iterable[rule_builder.OptionFilter[Any]]" = (),
    ) -> None:
        if len(item_names) != len(set(item_names)):
            raise ValueError(f"Duplicate items detected, likely typo, items: {item_names}")

        super().__init__(options=options)
        self.item_names = item_names

    @override
    def _instantiate(self, world: "AstalonWorld") -> "rule_builder.Rule.Resolved":
        if len(self.item_names) == 0:
            return rule_builder.True_.Resolved(player=world.player)
        if len(self.item_names) == 1:
            return Has(self.item_names[0]).resolve(world)

        new_clauses: list[rule_builder.Rule.Resolved] = []
        new_items: list[str] = []
        for item in self.item_names:
            if (
                item in VANILLA_CHARACTERS
                and world.options.randomize_characters.value == RandomizeCharacters.option_vanilla
            ):
                continue
            deps = ITEM_DEPS.get(item, [])
            if not deps:
                new_items.append(item.value)
                continue

            if len(deps) > 1:
                if world.options.randomize_characters.value == RandomizeCharacters.option_vanilla:
                    new_items.append(item.value)
                else:
                    new_clauses.append(
                        rule_builder.Or.Resolved(
                            tuple(HasAll.Resolved((d.value, item.value), player=world.player) for d in deps),
                            player=world.player,
                        )
                    )
                continue

            if (
                len(deps) == 1
                and deps[0] not in self.item_names
                and not (
                    deps[0] in VANILLA_CHARACTERS
                    and world.options.randomize_characters.value == RandomizeCharacters.option_vanilla
                )
            ):
                new_items.append(deps[0].value)

            new_items.append(item.value)

        if len(new_clauses) == 0 and len(new_items) == 0:
            return rule_builder.True_.Resolved(player=world.player)
        if len(new_items) == 1:
            new_clauses.append(Has.Resolved(new_items[0], player=world.player))
        elif len(new_items) > 1:
            new_clauses.append(HasAll.Resolved(tuple(new_items), player=world.player))
        if len(new_clauses) == 0:
            return rule_builder.False_.Resolved(player=world.player)
        if len(new_clauses) == 1:
            return new_clauses[0]
        return rule_builder.And.Resolved(tuple(new_clauses), player=world.player)

    @override
    def __str__(self) -> str:
        items = ", ".join([i.value for i in self.item_names])
        options = f", options={self.options}" if self.options else ""
        return f"{self.__class__.__name__}({items}{options})"

    @dataclasses.dataclass(frozen=True)
    class Resolved(rule_builder.HasAll.Resolved):
        @override
        def explain_json(self, state: "CollectionState | None" = None) -> "list[JSONMessagePart]":
            messages: list[JSONMessagePart] = [
                {"type": "text", "text": "Has "},
                {"type": "color", "color": "cyan", "text": "all"},
                {"type": "text", "text": " of ("},
            ]
            for i, item in enumerate(self.item_names):
                if i > 0:
                    messages.append({"type": "text", "text": ", "})
                messages.append(_printjson_item(item, self.player, state))
            messages.append({"type": "text", "text": ")"})
            return messages


@rule_builder.custom_rule(AstalonWorld)
class HasAny(rule_builder.Rule[AstalonWorld]):
    item_names: "tuple[ItemName | Events, ...]"

    def __init__(
        self,
        *item_names: "ItemName | Events",
        options: "Iterable[rule_builder.OptionFilter[Any]]" = (),
    ) -> None:
        if len(item_names) != len(set(item_names)):
            raise ValueError(f"Duplicate items detected, likely typo, items: {item_names}")

        super().__init__(options=options)
        self.item_names = item_names

    @override
    def _instantiate(self, world: "AstalonWorld") -> "rule_builder.Rule.Resolved":
        if len(self.item_names) == 0:
            return rule_builder.True_.Resolved(player=world.player)
        if len(self.item_names) == 1:
            return Has(self.item_names[0]).resolve(world)

        new_clauses: list[rule_builder.Rule.Resolved] = []
        new_items: list[str] = []
        for item in self.item_names:
            if (
                item in VANILLA_CHARACTERS
                and world.options.randomize_characters.value == RandomizeCharacters.option_vanilla
            ):
                return rule_builder.True_.Resolved(player=world.player)

            deps = ITEM_DEPS.get(item, [])
            if not deps:
                new_items.append(item.value)
                continue

            if len(deps) > 1:
                if world.options.randomize_characters.value == RandomizeCharacters.option_vanilla:
                    new_items.append(item.value)
                else:
                    new_clauses.append(
                        rule_builder.Or.Resolved(
                            tuple(HasAll.Resolved((d.value, item.value), player=world.player) for d in deps),
                            player=world.player,
                        )
                    )
                continue

            if (
                len(deps) == 1
                and deps[0] not in self.item_names
                and not (
                    deps[0] in VANILLA_CHARACTERS
                    and world.options.randomize_characters.value == RandomizeCharacters.option_vanilla
                )
            ):
                new_clauses.append(HasAll.Resolved((deps[0].value, item.value), player=world.player))
            else:
                new_items.append(item.value)

        if len(new_items) == 1:
            new_clauses.append(Has.Resolved(new_items[0], player=world.player))
        elif len(new_items) > 1:
            new_clauses.append(HasAny.Resolved(tuple(new_items), player=world.player))

        if len(new_clauses) == 0:
            return rule_builder.False_.Resolved(player=world.player)
        if len(new_clauses) == 1:
            return new_clauses[0]
        return rule_builder.Or.Resolved(tuple(new_clauses), player=world.player)

    @override
    def __str__(self) -> str:
        items = ", ".join([i.value for i in self.item_names])
        options = f", options={self.options}" if self.options else ""
        return f"{self.__class__.__name__}({items}{options})"

    @dataclasses.dataclass(frozen=True)
    class Resolved(rule_builder.HasAny.Resolved):
        @override
        def explain_json(self, state: "CollectionState | None" = None) -> "list[JSONMessagePart]":
            messages: list[JSONMessagePart] = [
                {"type": "text", "text": "Has "},
                {"type": "color", "color": "cyan", "text": "any"},
                {"type": "text", "text": " of ("},
            ]
            for i, item in enumerate(self.item_names):
                if i > 0:
                    messages.append({"type": "text", "text": ", "})
                messages.append(_printjson_item(item, self.player, state))
            messages.append({"type": "text", "text": ")"})
            return messages


@rule_builder.custom_rule(AstalonWorld)
class CanReachLocation(rule_builder.Rule[AstalonWorld]):
    location_name: "LocationName"

    @override
    def _instantiate(self, world: "AstalonWorld") -> "rule_builder.Rule.Resolved":
        location = world.get_location(self.location_name)
        if not location.parent_region:
            raise ValueError(f"Location {location.name} has no parent region")
        parent_region_name = location.parent_region.name
        return self.Resolved(self.location_name.value, parent_region_name, player=world.player)

    @override
    def __str__(self) -> str:
        options = f", options={self.options}" if self.options else ""
        return f"{self.__class__.__name__}({self.location_name.value}{options})"

    @dataclasses.dataclass(frozen=True)
    class Resolved(rule_builder.CanReachLocation.Resolved):
        pass


@rule_builder.custom_rule(AstalonWorld)
class CanReachRegion(rule_builder.Rule[AstalonWorld]):
    region_name: "RegionName"

    @override
    def _instantiate(self, world: "AstalonWorld") -> "rule_builder.Rule.Resolved":
        return self.Resolved(self.region_name.value, player=world.player)

    @override
    def __str__(self) -> str:
        options = f", options={self.options}" if self.options else ""
        return f"{self.__class__.__name__}({self.region_name.value}{options})"

    @dataclasses.dataclass(frozen=True)
    class Resolved(rule_builder.CanReachRegion.Resolved):
        pass


@rule_builder.custom_rule(AstalonWorld)
class CanReachEntrance(rule_builder.Rule[AstalonWorld]):
    from_region: "RegionName"
    to_region: "RegionName"

    @override
    def _instantiate(self, world: "AstalonWorld") -> "rule_builder.Rule.Resolved":
        entrance = f"{self.from_region.value} -> {self.to_region.value}"
        return self.Resolved(entrance, player=world.player)

    @override
    def __str__(self) -> str:
        options = f", options={self.options}" if self.options else ""
        return f"{self.__class__.__name__}({self.from_region.value} -> {self.to_region.value}{options})"

    @dataclasses.dataclass(frozen=True)
    class Resolved(rule_builder.CanReachEntrance.Resolved):
        pass


@dataclasses.dataclass(init=False)
class ToggleRule(HasAll):
    option_cls: "ClassVar[type[Option[int]]]"
    otherwise: bool = False

    @override
    def _instantiate(self, world: "AstalonWorld") -> "rule_builder.Rule.Resolved":
        if len(self.item_names) == 1:
            rule = Has(self.item_names[0], options=[rule_builder.OptionFilter(self.option_cls, 1)])
        else:
            rule = HasAll(*self.item_names, options=[rule_builder.OptionFilter(self.option_cls, 1)])

        if self.otherwise:
            return rule_builder.Or(
                rule,
                rule_builder.True_(options=[rule_builder.OptionFilter(self.option_cls, 0)]),
            ).resolve(world)

        return rule.resolve(world)


@rule_builder.custom_rule(AstalonWorld, init=False)
class HasWhite(ToggleRule):
    option_cls = RandomizeWhiteKeys

    def __init__(
        self,
        *doors: "WhiteDoor",
        otherwise: bool = False,
        options: "Iterable[rule_builder.OptionFilter[Any]]" = (),
    ) -> None:
        super().__init__(*doors, options=options)
        self.otherwise = otherwise


@rule_builder.custom_rule(AstalonWorld, init=False)
class HasBlue(ToggleRule):
    option_cls = RandomizeBlueKeys

    def __init__(
        self,
        *doors: "BlueDoor",
        otherwise: bool = False,
        options: "Iterable[rule_builder.OptionFilter[Any]]" = (),
    ) -> None:
        super().__init__(*doors, options=options)
        self.otherwise = otherwise


@rule_builder.custom_rule(AstalonWorld, init=False)
class HasRed(ToggleRule):
    option_cls = RandomizeRedKeys

    def __init__(
        self,
        *doors: "RedDoor",
        otherwise: bool = False,
        options: "Iterable[rule_builder.OptionFilter[Any]]" = (),
    ) -> None:
        super().__init__(*doors, options=options)
        self.otherwise = otherwise


@rule_builder.custom_rule(AstalonWorld, init=False)
class HasSwitch(ToggleRule):
    option_cls = RandomizeSwitches

    def __init__(
        self,
        *switches: "Switch | Crystal | Face",
        otherwise: bool = False,
        options: "Iterable[rule_builder.OptionFilter[Any]]" = (),
    ) -> None:
        super().__init__(*switches, options=options)
        self.otherwise = otherwise


@rule_builder.custom_rule(AstalonWorld, init=False)
class HasElevator(HasAll):
    def __init__(self, elevator: "Elevator", *, options: "Iterable[rule_builder.OptionFilter[Any]]" = ()) -> None:
        super().__init__(
            KeyItem.ASCENDANT_KEY,
            elevator,
            options=[*options, rule_builder.OptionFilter(RandomizeElevator, RandomizeElevator.option_true)],
        )


@rule_builder.custom_rule(AstalonWorld)
class HasGoal(rule_builder.Rule[AstalonWorld]):
    @override
    def _instantiate(self, world: "AstalonWorld") -> "rule_builder.Rule.Resolved":
        if world.options.goal.value != Goal.option_eye_hunt:
            return rule_builder.True_.Resolved(player=world.player)
        return Has.Resolved(
            Eye.GOLD.value,
            count=world.options.additional_eyes_required.value,
            player=world.player,
        )


@rule_builder.custom_rule(AstalonWorld)
class HardLogic(rule_builder.Rule[AstalonWorld]):
    child: "rule_builder.Rule[AstalonWorld]"

    @override
    def _instantiate(self, world: "AstalonWorld") -> "rule_builder.Rule.Resolved":
        if world.options.difficulty.value == Difficulty.option_hard:
            return self.child.resolve(world)
        if getattr(world.multiworld, "generation_is_fake", False):
            return self.Resolved(self.child.resolve(world), player=world.player)
        return rule_builder.False_.Resolved(player=world.player)

    @override
    def __str__(self) -> str:
        return f"HardLogic[{self.child!s}]"

    @dataclasses.dataclass(frozen=True)
    class Resolved(rule_builder.Rule.Resolved):
        child: "rule_builder.Rule.Resolved"
        rule_name: ClassVar[str] = "HardLogic"

        @override
        def _evaluate(self, state: "CollectionState") -> bool:
            return state.has(Events.FAKE_OOL_ITEM.value, self.player) and self.child.test(state)

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            deps = self.child.item_dependencies()
            deps.setdefault(Events.FAKE_OOL_ITEM.value, set()).add(id(self))
            return deps

        @override
        def indirect_regions(self) -> tuple[str, ...]:
            return self.child.indirect_regions()

        @override
        def explain_json(self, state: "CollectionState | None" = None) -> "list[JSONMessagePart]":
            messages: "list[JSONMessagePart]" = [
                {"type": "color", "color": "glitched", "text": "Hard Logic ["},
            ]
            messages.extend(self.child.explain_json(state))
            messages.append({"type": "color", "color": "glitched", "text": "]"})
            return messages
