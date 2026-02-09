import dataclasses
from collections.abc import Iterable
from enum import Enum
from typing import ClassVar, cast

from typing_extensions import override

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from Options import Option
from rule_builder import rules
from rule_builder.options import OptionFilter

from ..bases import AstalonWorldBase
from ..constants import GAME_NAME
from ..items import (
    BlueDoor,
    Crystal,
    Elevator,
    Events,
    Eye,
    Face,
    ItemName,
    KeyItem,
    RedDoor,
    Switch,
    WhiteDoor,
)
from ..locations import LocationName
from ..options import (
    Difficulty,
    Goal,
    RandomizeBlueKeys,
    RandomizeElevator,
    RandomizeRedKeys,
    RandomizeSwitches,
    RandomizeWhiteKeys,
)
from ..regions import RegionName


def as_str(value: Enum | str | None) -> str:
    if value is None:
        return ""
    return value.value if isinstance(value, Enum) else value


@dataclasses.dataclass(init=False)
class Has(rules.Has[AstalonWorldBase], game=GAME_NAME):
    @override
    def __init__(
        self,
        item_name: ItemName | Events,
        count: int = 1,
        *,
        options: Iterable[OptionFilter] = (),
        filtered_resolution: bool = False,
    ) -> None:
        super().__init__(as_str(item_name), count, options=options, filtered_resolution=filtered_resolution)


@dataclasses.dataclass(init=False)
class HasAll(rules.HasAll[AstalonWorldBase], game=GAME_NAME):
    @override
    def __init__(
        self,
        *item_names: ItemName | Events,
        options: Iterable[OptionFilter] = (),
    ) -> None:
        names = [as_str(name) for name in item_names]
        if len(names) != len(set(names)):
            raise ValueError(f"Duplicate items detected, likely typo, items: {names}")

        super().__init__(*names, options=options)


@dataclasses.dataclass(init=False)
class HasAny(rules.HasAny[AstalonWorldBase], game=GAME_NAME):
    @override
    def __init__(
        self,
        *item_names: ItemName | Events,
        options: Iterable[OptionFilter] = (),
    ) -> None:
        names = [as_str(name) for name in item_names]
        if len(names) != len(set(names)):
            raise ValueError(f"Duplicate items detected, likely typo, items: {names}")

        super().__init__(*names, options=options)


@dataclasses.dataclass(init=False)
class CanReachLocation(rules.CanReachLocation[AstalonWorldBase], game=GAME_NAME):
    @override
    def __init__(
        self,
        location_name: LocationName,
        parent_region_name: RegionName | None = None,
        skip_indirect_connection: bool = False,
        *,
        options: Iterable[OptionFilter] = (),
    ) -> None:
        super().__init__(as_str(location_name), as_str(parent_region_name), skip_indirect_connection, options=options)


@dataclasses.dataclass(init=False)
class CanReachRegion(rules.CanReachRegion[AstalonWorldBase], game=GAME_NAME):
    @override
    def __init__(
        self,
        region_name: RegionName,
        *,
        options: Iterable[OptionFilter] = (),
    ) -> None:
        super().__init__(as_str(region_name), options=options)


@dataclasses.dataclass(init=False)
class CanReachEntrance(rules.CanReachEntrance[AstalonWorldBase], game=GAME_NAME):
    @override
    def __init__(
        self,
        from_region: RegionName,
        to_region: RegionName,
        *,
        options: Iterable[OptionFilter] = (),
    ) -> None:
        entrance_name = f"{as_str(from_region)} -> {as_str(to_region)}"
        super().__init__(entrance_name, as_str(from_region), options=options)


@dataclasses.dataclass(init=False)
class ToggleRule(HasAll, game=GAME_NAME):
    option_cls: ClassVar[type[Option[int]]]
    otherwise: bool = False

    @override
    def _instantiate(self, world: AstalonWorldBase) -> rules.Rule.Resolved:
        items = tuple(cast(ItemName | Events, item) for item in self.item_names)
        if len(items) == 1:
            rule = Has(items[0], options=[OptionFilter(self.option_cls, 1)])
        else:
            rule = HasAll(*items, options=[OptionFilter(self.option_cls, 1)])

        if self.otherwise:
            return rules.Or(
                rule,
                rules.True_(options=[OptionFilter(self.option_cls, 0)]),
            ).resolve(world)

        return rule.resolve(world)


@dataclasses.dataclass(init=False)
class HasWhite(ToggleRule, game=GAME_NAME):
    option_cls: ClassVar[type[Option[int]]] = RandomizeWhiteKeys

    def __init__(
        self,
        *doors: WhiteDoor,
        otherwise: bool = False,
        options: Iterable[OptionFilter] = (),
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
        options: Iterable[OptionFilter] = (),
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
        options: Iterable[OptionFilter] = (),
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
        options: Iterable[OptionFilter] = (),
    ) -> None:
        super().__init__(*switches, options=options)
        self.otherwise: bool = otherwise


@dataclasses.dataclass(init=False)
class HasElevator(HasAll, game=GAME_NAME):
    def __init__(self, elevator: Elevator, *, options: Iterable[OptionFilter] = ()) -> None:
        super().__init__(
            KeyItem.ASCENDANT_KEY,
            elevator,
            options=[*options, OptionFilter(RandomizeElevator, RandomizeElevator.option_true)],
        )


@dataclasses.dataclass()
class HasGoal(rules.Rule[AstalonWorldBase], game=GAME_NAME):
    @override
    def _instantiate(self, world: AstalonWorldBase) -> rules.Rule.Resolved:
        if world.options.goal.value != Goal.option_eye_hunt:
            return rules.True_().resolve(world)
        return Has(Eye.GOLD, world.options.additional_eyes_required.value).resolve(world)


@dataclasses.dataclass()
class HardLogic(rules.WrapperRule[AstalonWorldBase], game=GAME_NAME):
    @override
    def _instantiate(self, world: AstalonWorldBase) -> rules.Rule.Resolved:
        if world.options.difficulty.value == Difficulty.option_hard:
            return self.child.resolve(world)
        if getattr(world.multiworld, "generation_is_fake", False):
            return self.Resolved(
                self.child.resolve(world),
                player=world.player,
                caching_enabled=getattr(world, "rule_caching_enabled", False),
            )
        return rules.False_().resolve(world)

    class Resolved(rules.WrapperRule.Resolved):
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


@dataclasses.dataclass()
class CampfireWarp(rules.True_[AstalonWorldBase], game=GAME_NAME):
    name: str

    @override
    def _instantiate(self, world: AstalonWorldBase) -> "Resolved":
        return self.Resolved(
            self.name,
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )

    class Resolved(rules.True_.Resolved):
        name: str

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            return [{"type": "color", "color": "green", "text": f"Campfire Warp to {self.name}"}]

        @override
        def __str__(self) -> str:
            return f"Campfire Warp to {self.name}"
