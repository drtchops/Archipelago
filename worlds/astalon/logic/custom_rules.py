import dataclasses
from collections.abc import Iterable
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar

from typing_extensions import override

import rule_builder
from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from Options import Option

from ..constants import GAME_NAME
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
from ..locations import LocationName
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
from ..regions import RegionName

if TYPE_CHECKING:
    from ..world import AstalonWorld


ITEM_DEPS: dict[str, tuple[str, ...]] = {
    KeyItem.CLOAK.value: (Character.ALGUS.value,),
    KeyItem.SWORD.value: (Character.ARIAS.value,),
    KeyItem.BOOTS.value: (Character.ARIAS.value,),
    KeyItem.CLAW.value: (Character.KYULI.value,),
    KeyItem.BOW.value: (Character.KYULI.value,),
    KeyItem.BLOCK.value: (Character.ZEEK.value,),
    KeyItem.STAR.value: (Character.BRAM.value,),
    KeyItem.BANISH.value: (Character.ALGUS.value, Character.ZEEK.value),
    KeyItem.GAUNTLET.value: (Character.ARIAS.value, Character.BRAM.value),
    ShopUpgrade.ALGUS_ARCANIST.value: (Character.ALGUS.value,),
    ShopUpgrade.ALGUS_METEOR.value: (Character.ALGUS.value,),
    ShopUpgrade.ALGUS_SHOCK.value: (Character.ALGUS.value,),
    ShopUpgrade.ARIAS_GORGONSLAYER.value: (Character.ARIAS.value,),
    ShopUpgrade.ARIAS_LAST_STAND.value: (Character.ARIAS.value,),
    ShopUpgrade.ARIAS_LIONHEART.value: (Character.ARIAS.value,),
    ShopUpgrade.KYULI_ASSASSIN.value: (Character.KYULI.value,),
    ShopUpgrade.KYULI_BULLSEYE.value: (Character.KYULI.value,),
    ShopUpgrade.KYULI_RAY.value: (Character.KYULI.value,),
    ShopUpgrade.ZEEK_JUNKYARD.value: (Character.ZEEK.value,),
    ShopUpgrade.ZEEK_ORBS.value: (Character.ZEEK.value,),
    ShopUpgrade.ZEEK_LOOT.value: (Character.ZEEK.value,),
    ShopUpgrade.BRAM_AXE.value: (Character.BRAM.value,),
    ShopUpgrade.BRAM_HUNTER.value: (Character.BRAM.value,),
    ShopUpgrade.BRAM_WHIPLASH.value: (Character.BRAM.value,),
}

VANILLA_CHARACTERS: frozenset[str] = frozenset((Character.ALGUS.value, Character.ARIAS.value, Character.KYULI.value))

characters_off = [rule_builder.OptionFilter(RandomizeCharacters, RandomizeCharacters.option_vanilla)]
characters_on = [rule_builder.OptionFilter(RandomizeCharacters, RandomizeCharacters.option_vanilla, operator="gt")]


def as_str(value: Enum | str) -> str:
    return value.value if isinstance(value, Enum) else value


@dataclasses.dataclass(init=False)
class Has(rule_builder.Has["AstalonWorld"], game=GAME_NAME):
    @override
    def __init__(
        self,
        item_name: ItemName | Events | str,
        count: int = 1,
        *,
        options: Iterable[rule_builder.OptionFilter[Any]] = (),
    ) -> None:
        super().__init__(as_str(item_name), count, options=options)

    @override
    def _instantiate(self, world: "AstalonWorld") -> rule_builder.Rule.Resolved:
        default = self.Resolved(self.item_name, self.count, player=world.player)

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
                return HasAll.Resolved((deps[0], self.item_name), player=world.player)
            return rule_builder.Or.Resolved(
                tuple(world.get_cached_rule(HasAll.Resolved((d, self.item_name), player=world.player)) for d in deps),
                player=world.player,
            )

        return default


@dataclasses.dataclass(init=False)
class HasAll(rule_builder.HasAll["AstalonWorld"], game=GAME_NAME):
    @override
    def __init__(
        self,
        *item_names: ItemName | Events | str,
        options: Iterable[rule_builder.OptionFilter[Any]] = (),
    ) -> None:
        names = [as_str(name) for name in item_names]
        if len(names) != len(set(names)):
            raise ValueError(f"Duplicate items detected, likely typo, items: {names}")

        super().__init__(*names, options=options)

    @override
    def _instantiate(self, world: "AstalonWorld") -> rule_builder.Rule.Resolved:
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
                new_items.append(item)
                continue

            if len(deps) > 1:
                if world.options.randomize_characters.value == RandomizeCharacters.option_vanilla:
                    new_items.append(item)
                else:
                    new_clauses.append(
                        rule_builder.Or.Resolved(
                            tuple(world.get_cached_rule(HasAll.Resolved((d, item), player=world.player)) for d in deps),
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
                new_items.append(deps[0])

            new_items.append(item)

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
        return rule_builder.And.Resolved(tuple(world.get_cached_rule(c) for c in new_clauses), player=world.player)


@dataclasses.dataclass(init=False)
class HasAny(rule_builder.HasAny["AstalonWorld"], game=GAME_NAME):
    @override
    def __init__(
        self,
        *item_names: ItemName | Events | str,
        options: Iterable[rule_builder.OptionFilter[Any]] = (),
    ) -> None:
        names = [as_str(name) for name in item_names]
        if len(names) != len(set(names)):
            raise ValueError(f"Duplicate items detected, likely typo, items: {names}")

        super().__init__(*names, options=options)

    @override
    def _instantiate(self, world: "AstalonWorld") -> rule_builder.Rule.Resolved:
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
                new_items.append(item)
                continue

            if len(deps) > 1:
                if world.options.randomize_characters.value == RandomizeCharacters.option_vanilla:
                    new_items.append(item)
                else:
                    new_clauses.append(
                        rule_builder.Or.Resolved(
                            tuple(world.get_cached_rule(HasAll.Resolved((d, item), player=world.player)) for d in deps),
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
                new_clauses.append(HasAll.Resolved((deps[0], item), player=world.player))
            else:
                new_items.append(item)

        if len(new_items) == 1:
            new_clauses.append(Has.Resolved(new_items[0], player=world.player))
        elif len(new_items) > 1:
            new_clauses.append(HasAny.Resolved(tuple(new_items), player=world.player))

        if len(new_clauses) == 0:
            return rule_builder.False_.Resolved(player=world.player)
        if len(new_clauses) == 1:
            return new_clauses[0]
        return rule_builder.Or.Resolved(tuple(world.get_cached_rule(c) for c in new_clauses), player=world.player)


@dataclasses.dataclass(init=False)
class CanReachLocation(rule_builder.CanReachLocation["AstalonWorld"], game=GAME_NAME):
    @override
    def __init__(
        self,
        location_name: LocationName | str,
        parent_region_name: RegionName | str = "",
        skip_indirect_connection: bool = False,
        *,
        options: Iterable[rule_builder.OptionFilter[Any]] = (),
    ) -> None:
        super().__init__(as_str(location_name), as_str(parent_region_name), skip_indirect_connection, options=options)


@dataclasses.dataclass(init=False)
class CanReachRegion(rule_builder.CanReachRegion["AstalonWorld"], game=GAME_NAME):
    @override
    def __init__(
        self,
        region_name: RegionName | str,
        *,
        options: Iterable[rule_builder.OptionFilter[Any]] = (),
    ) -> None:
        super().__init__(as_str(region_name), options=options)


@dataclasses.dataclass(init=False)
class CanReachEntrance(rule_builder.CanReachEntrance["AstalonWorld"], game=GAME_NAME):
    @override
    def __init__(
        self,
        from_region: RegionName | str,
        to_region: RegionName | str,
        *,
        options: Iterable[rule_builder.OptionFilter[Any]] = (),
    ) -> None:
        entrance_name = f"{as_str(from_region)} -> {as_str(to_region)}"
        super().__init__(entrance_name, as_str(from_region), options=options)


@dataclasses.dataclass(init=False)
class ToggleRule(HasAll, game=GAME_NAME):
    option_cls: ClassVar[type[Option[int]]]
    otherwise: bool = False

    @override
    def _instantiate(self, world: "AstalonWorld") -> rule_builder.Rule.Resolved:
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


@dataclasses.dataclass(init=False)
class HasWhite(ToggleRule, game=GAME_NAME):
    option_cls: ClassVar[type[Option[int]]] = RandomizeWhiteKeys

    def __init__(
        self,
        *doors: WhiteDoor,
        otherwise: bool = False,
        options: Iterable[rule_builder.OptionFilter[Any]] = (),
    ) -> None:
        super().__init__(*doors, options=options)
        self.otherwise: bool = otherwise


@dataclasses.dataclass(init=False)
class HasBlue(ToggleRule, game=GAME_NAME):
    option_cls: ClassVar[type[Option[int]]] = RandomizeBlueKeys

    def __init__(
        self,
        *doors: BlueDoor,
        otherwise: bool = False,
        options: Iterable[rule_builder.OptionFilter[Any]] = (),
    ) -> None:
        super().__init__(*doors, options=options)
        self.otherwise: bool = otherwise


@dataclasses.dataclass(init=False)
class HasRed(ToggleRule, game=GAME_NAME):
    option_cls: ClassVar[type[Option[int]]] = RandomizeRedKeys

    def __init__(
        self,
        *doors: RedDoor,
        otherwise: bool = False,
        options: Iterable[rule_builder.OptionFilter[Any]] = (),
    ) -> None:
        super().__init__(*doors, options=options)
        self.otherwise: bool = otherwise


@dataclasses.dataclass(init=False)
class HasSwitch(ToggleRule, game=GAME_NAME):
    option_cls: ClassVar[type[Option[int]]] = RandomizeSwitches

    def __init__(
        self,
        *switches: Switch | Crystal | Face,
        otherwise: bool = False,
        options: Iterable[rule_builder.OptionFilter[Any]] = (),
    ) -> None:
        super().__init__(*switches, options=options)
        self.otherwise: bool = otherwise


@dataclasses.dataclass(init=False)
class HasElevator(HasAll, game=GAME_NAME):
    def __init__(self, elevator: Elevator, *, options: Iterable[rule_builder.OptionFilter[Any]] = ()) -> None:
        super().__init__(
            KeyItem.ASCENDANT_KEY,
            elevator,
            options=[*options, rule_builder.OptionFilter(RandomizeElevator, RandomizeElevator.option_true)],
        )


@dataclasses.dataclass()
class HasGoal(rule_builder.Rule["AstalonWorld"], game=GAME_NAME):
    @override
    def _instantiate(self, world: "AstalonWorld") -> rule_builder.Rule.Resolved:
        if world.options.goal.value != Goal.option_eye_hunt:
            return rule_builder.True_.Resolved(player=world.player)
        return Has.Resolved(
            Eye.GOLD.value,
            count=world.options.additional_eyes_required.value,
            player=world.player,
        )


@dataclasses.dataclass()
class HardLogic(rule_builder.Wrapper["AstalonWorld"], game=GAME_NAME):
    @override
    def _instantiate(self, world: "AstalonWorld") -> rule_builder.Rule.Resolved:
        if world.options.difficulty.value == Difficulty.option_hard:
            return self.child.resolve(world)
        if getattr(world.multiworld, "generation_is_fake", False):
            return self.Resolved(world.get_cached_rule(self.child.resolve(world)), player=world.player)
        return rule_builder.False_.Resolved(player=world.player)

    class Resolved(rule_builder.Wrapper.Resolved):
        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return state.has(Events.FAKE_OOL_ITEM.value, self.player) and self.child(state)

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            deps = super().item_dependencies()
            deps.setdefault(Events.FAKE_OOL_ITEM.value, set()).add(id(self))
            return deps

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            messages: list[JSONMessagePart] = [
                {"type": "color", "color": "glitched", "text": "Hard Logic ["},
            ]
            messages.extend(self.child.explain_json(state))
            messages.append({"type": "color", "color": "glitched", "text": "]"})
            return messages
