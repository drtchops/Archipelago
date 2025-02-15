import dataclasses
from copy import copy
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Union

from .items import KeyItem

if TYPE_CHECKING:
    from BaseClasses import CollectionState
    from Options import CommonOptions, Option

    from .items import BlueDoor, Crystal, Elevator, Face, ItemName, RedDoor, Switch, WhiteDoor
    from .regions import RegionName

hit = 0
miss = 0


@dataclasses.dataclass()
class Rule:
    _: dataclasses.KW_ONLY
    result: bool = dataclasses.field(default=True, repr=False)
    stale: bool = dataclasses.field(default=True, repr=False)
    player: int = -1
    opts: Tuple[Tuple[str, Any], ...] = ()

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
            if operator == "lt" and opt.value >= value:
                return False
        return True

    def evaluate(self, state: "CollectionState") -> None:
        self.result = self._evaluate(state)
        self.stale = False

    def test(self, state) -> bool:
        if self.stale:
            global miss  # noqa: PLW0603
            miss += 1
            self.evaluate(state)
        else:
            global hit  # noqa: PLW0603
            hit += 1
        return self.result

    def actualize(self, player: int, options: "CommonOptions") -> "Rule":
        if not self._pass_opts(options):
            return False_(player=player)

        new_rule = copy(self)
        new_rule.player = player
        return new_rule

    def deps(self) -> "Dict[str, List[Rule]]":
        return {}


@dataclasses.dataclass()
class True_(Rule):
    def _evaluate(self, state: "CollectionState") -> bool:
        return True


@dataclasses.dataclass()
class False_(Rule):
    def _evaluate(self, state: "CollectionState") -> bool:
        return False


@dataclasses.dataclass(init=False)
class NestedRule(Rule):
    children: "Tuple[Rule, ...]"

    def __init__(self, *children: "Rule", **kwargs) -> None:
        self.children = children
        super().__init__(**kwargs)

    @property
    def stale(self) -> bool:  # type: ignore
        for rule in self.children:
            if rule.stale:
                return True
        return False

    @stale.setter
    def stale(self, value: bool) -> None:  # type: ignore
        # dynamically calculated
        pass

    def deps(self) -> "Dict[str, List[Rule]]":
        deps: Dict[str, List[Rule]] = {}
        for child in self.children:
            for item_name, rules in child.deps().items():
                if item_name in deps:
                    deps[item_name] += rules
                else:
                    deps[item_name] = rules
        return deps


@dataclasses.dataclass(init=False)
class And(NestedRule):
    def _evaluate(self, state: "CollectionState") -> bool:
        for rule in self.children:
            if not rule.test(state):
                return False
        return True

    def actualize(self, player: int, options: "CommonOptions") -> "Rule":
        if not self._pass_opts(options):
            return False_(player=player)

        true_rule: Union[True_, None] = None
        new_children = []
        for child in self.children:
            new_child = child.actualize(player, options)
            if new_child is None:
                continue
            if isinstance(new_child, False_):
                # false always wins
                return new_child
            if isinstance(new_child, True_):
                # dedupe trues
                true_rule = new_child
                continue
            new_children.append(new_child)

        if not new_children:
            return true_rule or False_(player=player)
        if len(new_children) == 1:
            return new_children[0]

        new_rule = copy(self)
        new_rule.player = player
        new_rule.children = tuple(new_children)
        return new_rule


@dataclasses.dataclass(init=False)
class Or(NestedRule):
    def _evaluate(self, state: "CollectionState") -> bool:
        for rule in self.children:
            if rule.test(state):
                return True
        return False

    def actualize(self, player: int, options: "CommonOptions") -> "Rule":
        if not self._pass_opts(options):
            return False_(player=player)

        new_children = []
        for child in self.children:
            new_child = child.actualize(player, options)
            if new_child is None:
                continue
            if isinstance(new_child, True_):
                # true always wins
                return new_child
            if isinstance(new_child, False_):
                # falses can be ignored
                continue
            new_children.append(new_child)

        if not new_children:
            return False_(player=player)
        if len(new_children) == 1:
            return new_children[0]

        new_rule = copy(self)
        new_rule.player = player
        new_rule.children = tuple(new_children)
        return new_rule


@dataclasses.dataclass(init=False)
class Has(Rule):
    item: str
    count: int

    def __init__(self, item: "ItemName", count: int = 1, **kwargs) -> None:
        self.item = item.value if hasattr(item, "value") else item
        self.count = count
        super().__init__(**kwargs)

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.has(self.item, self.player, count=self.count)

    def deps(self) -> Dict[str, List[Rule]]:
        return {self.item: [self]}


@dataclasses.dataclass(init=False)
class HasAll(Rule):
    items: Tuple[str, ...]

    def __init__(self, *items: "ItemName", **kwargs) -> None:
        self.items = tuple(item.value if hasattr(item, "value") else item for item in items)
        super().__init__(**kwargs)

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.has_all(self.items, self.player)

    def deps(self) -> Dict[str, List[Rule]]:
        return {item: [self] for item in self.items}


@dataclasses.dataclass(init=False)
class HasAny(Rule):
    items: Tuple[str, ...]

    def __init__(self, *items: "ItemName", **kwargs) -> None:
        self.items = tuple(item.value if hasattr(item, "value") else item for item in items)
        super().__init__(**kwargs)

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.has_any(self.items, self.player)

    def deps(self) -> Dict[str, List[Rule]]:
        return {item: [self] for item in self.items}


@dataclasses.dataclass(init=False)
class CanReachRegion(Rule):
    region: str
    # TODO: indirect

    def __init__(self, region: "RegionName", **kwargs) -> None:
        self.region = region.value if hasattr(region, "value") else region
        super().__init__(**kwargs)

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.can_reach_region(self.region, self.player)


@dataclasses.dataclass(init=False)
class HasWhiteDoor(Has):
    def __init__(self, door: "WhiteDoor", **kwargs) -> None:
        super().__init__(door, opt=(("randomize_white_keys", 1),), **kwargs)


@dataclasses.dataclass(init=False)
class HasWhiteDoors(HasAll):
    def __init__(self, *doors: "WhiteDoor", **kwargs) -> None:
        super().__init__(*doors, opt=(("randomize_white_keys", 1),), **kwargs)


@dataclasses.dataclass(init=False)
class HasBlueDoor(Has):
    def __init__(self, door: "BlueDoor", **kwargs) -> None:
        super().__init__(door, opt=(("randomize_blue_keys", 1),), **kwargs)


@dataclasses.dataclass(init=False)
class HasBlueDoors(HasAll):
    def __init__(self, *doors: "BlueDoor", **kwargs) -> None:
        super().__init__(*doors, opt=(("randomize_blue_keys", 1),), **kwargs)


@dataclasses.dataclass(init=False)
class HasRedDoor(Has):
    def __init__(self, door: "RedDoor", **kwargs) -> None:
        super().__init__(door, opt=(("randomize_red_keys", 1),), **kwargs)


@dataclasses.dataclass(init=False)
class HasSwitch(Has):
    def __init__(self, switch: "Union[Switch, Crystal, Face]", **kwargs) -> None:
        super().__init__(switch, opt=(("randomize_switches", 1),), **kwargs)


@dataclasses.dataclass(init=False)
class HasSwitches(HasAll):
    def __init__(self, *switches: "Union[Switch, Crystal, Face]", **kwargs) -> None:
        super().__init__(*switches, opt=(("randomize_switches", 1),), **kwargs)


@dataclasses.dataclass(init=False)
class HasElevator(HasAll):
    def __init__(self, elevator: "Elevator", **kwargs) -> None:
        super().__init__(KeyItem.ASCENDANT_KEY, elevator, opt=(("randomize_elevator", 1),), **kwargs)
