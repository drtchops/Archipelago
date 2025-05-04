import dataclasses
import itertools
from typing import TYPE_CHECKING, ClassVar, Dict, List, Optional, Set, Tuple

from ..items import Events
from ..regions import RegionName

if TYPE_CHECKING:
    from BaseClasses import CollectionState
    from NetUtils import JSONMessagePart


def _printjson_item(item: str, player: int, state: "CollectionState | None" = None) -> "JSONMessagePart":
    if state:
        color = "green" if state.has(item, player) else "salmon"
        if item == Events.FAKE_OOL_ITEM:
            color = "glitched"
        return {"type": "color", "color": color, "text": item}
    else:
        return {"type": "item_name", "flags": 0b001, "text": item, "player": player}


@dataclasses.dataclass(kw_only=True, frozen=True)
class RuleInstance:
    player: int
    cacheable: bool = dataclasses.field(repr=False, default=True)

    always_true: ClassVar = False
    always_false: ClassVar = False

    def __hash__(self) -> int:
        return hash((self.__class__.__name__, *[getattr(self, f.name) for f in dataclasses.fields(self)]))

    def _evaluate(self, state: "CollectionState") -> bool: ...

    def evaluate(self, state: "CollectionState") -> bool:
        result = self._evaluate(state)
        if self.cacheable:
            state._astalon_rule_results[self.player][id(self)] = result  # type: ignore
        return result

    def test(self, state: "CollectionState") -> bool:
        cached_result = None
        if self.cacheable:
            cached_result = state._astalon_rule_results[self.player].get(id(self))  # type: ignore
        if cached_result is not None:
            return cached_result
        return self.evaluate(state)

    def deps(self) -> "Dict[str, Set[int]]":
        return {}

    def indirect(self) -> "Tuple[RegionName, ...]":
        return ()

    def serialize(self) -> str:
        return f"{self.__class__.__name__}()"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        return [{"type": "text", "text": self.__class__.__name__}]


@dataclasses.dataclass(frozen=True)
class TrueInstance(RuleInstance):
    cacheable: bool = dataclasses.field(repr=False, default=False, init=False)

    always_true: ClassVar = True

    def __hash__(self) -> int:
        return super().__hash__()

    def _evaluate(self, state: "CollectionState") -> bool:
        return True

    def serialize(self) -> str:
        return "True"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        return [{"type": "color", "color": "green", "text": "True"}]


@dataclasses.dataclass(frozen=True)
class FalseInstance(RuleInstance):
    cacheable: bool = dataclasses.field(repr=False, default=False, init=False)

    always_false: ClassVar = True

    def __hash__(self) -> int:
        return super().__hash__()

    def _evaluate(self, state: "CollectionState") -> bool:
        return False

    def serialize(self) -> str:
        return "False"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        return [{"type": "color", "color": "salmon", "text": "False"}]


@dataclasses.dataclass(frozen=True)
class NestedRuleInstance(RuleInstance):
    children: "Tuple[RuleInstance, ...]"

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

    def simplify(self) -> "RuleInstance":
        return self


@dataclasses.dataclass(frozen=True)
class AndInstance(NestedRuleInstance):
    def _evaluate(self, state: "CollectionState") -> bool:
        for rule in self.children:
            if not rule.test(state):
                return False
        return True

    def serialize(self) -> str:
        return f"({' + '.join(child.serialize() for child in self.children)})"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        messages: List[JSONMessagePart] = [{"type": "text", "text": "("}]
        for i, child in enumerate(self.children):
            if i > 0:
                messages.append({"type": "text", "text": " & "})
            messages.extend(child.explain(state))
        messages.append({"type": "text", "text": ")"})
        return messages

    def simplify(self) -> "RuleInstance":
        children_to_process = list(self.children)
        clauses: List[RuleInstance] = []
        items: List[str] = []
        true_rule: Optional[RuleInstance] = None

        while children_to_process:
            child = children_to_process.pop(0)
            if child.always_false:
                # false always wins
                return child
            if child.always_true:
                # dedupe trues
                true_rule = child
                continue
            if isinstance(child, AndInstance):
                children_to_process.extend(child.children)
                continue

            if isinstance(child, HasInstance) and child.count == 1:
                items.append(child.item)
            elif isinstance(child, HasAllInstance):
                items.extend(child.items)
            else:
                clauses.append(child)

        if not clauses and not items:
            return true_rule or FalseInstance(player=self.player)
        if items:
            if len(items) == 1:
                item_rule = HasInstance(items[0], player=self.player)
            else:
                item_rule = HasAllInstance(tuple(items), player=self.player)
            if not clauses:
                return item_rule
            clauses.append(item_rule)

        if len(clauses) == 1:
            return clauses[0]
        return AndInstance(
            tuple(clauses),
            player=self.player,
            cacheable=self.cacheable and all(c.cacheable for c in clauses),
        )


@dataclasses.dataclass(frozen=True)
class OrInstance(NestedRuleInstance):
    def _evaluate(self, state: "CollectionState") -> bool:
        for rule in self.children:
            if rule.test(state):
                return True
        return False

    def serialize(self) -> str:
        return f"({' | '.join(child.serialize() for child in self.children)})"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        messages: List[JSONMessagePart] = [{"type": "text", "text": "("}]
        for i, child in enumerate(self.children):
            if i > 0:
                messages.append({"type": "text", "text": " | "})
            messages.extend(child.explain(state))
        messages.append({"type": "text", "text": ")"})
        return messages

    def simplify(self) -> "RuleInstance":
        children_to_process = list(self.children)
        clauses: List[RuleInstance] = []
        items: List[str] = []

        while children_to_process:
            child = children_to_process.pop(0)
            if child.always_true:
                # true always wins
                return child
            if child.always_false:
                # falses can be ignored
                continue
            if isinstance(child, OrInstance):
                children_to_process.extend(child.children)
                continue

            if isinstance(child, HasInstance) and child.count == 1:
                items.append(child.item)
            elif isinstance(child, HasAnyInstance):
                items.extend(child.items)
            else:
                clauses.append(child)

        if not clauses and not items:
            return FalseInstance(player=self.player)
        if items:
            if len(items) == 1:
                item_rule = HasInstance(items[0], player=self.player)
            else:
                item_rule = HasAnyInstance(tuple(items), player=self.player)
            if not clauses:
                return item_rule
            clauses.append(item_rule)

        if len(clauses) == 1:
            return clauses[0]
        return OrInstance(
            tuple(clauses),
            player=self.player,
            cacheable=self.cacheable and all(c.cacheable for c in clauses),
        )


@dataclasses.dataclass(frozen=True)
class HasInstance(RuleInstance):
    item: str
    count: int = 1

    def __hash__(self) -> int:
        return super().__hash__()

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.has(self.item, self.player, count=self.count)

    def deps(self) -> Dict[str, Set[int]]:
        return {self.item: {id(self)}}

    def serialize(self) -> str:
        count_display = f", count={self.count}" if self.count > 1 else ""
        return f"Has({self.item}{count_display})"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        messages: List[JSONMessagePart] = [{"type": "text", "text": "Has "}]
        if self.count > 1:
            messages.append({"type": "color", "color": "cyan", "text": str(self.count)})
            messages.append({"type": "text", "text": "x "})
        messages.append(_printjson_item(self.item, self.player, state))
        return messages


@dataclasses.dataclass(frozen=True)
class HasAllInstance(RuleInstance):
    items: Tuple[str, ...]

    def __hash__(self) -> int:
        return super().__hash__()

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.has_all(self.items, self.player)

    def deps(self) -> Dict[str, Set[int]]:
        return {item: {id(self)} for item in self.items}

    def serialize(self) -> str:
        return f"HasAll({', '.join(self.items)})"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        messages: List[JSONMessagePart] = [
            {"type": "text", "text": "Has "},
            {"type": "color", "color": "cyan", "text": "all"},
            {"type": "text", "text": " of ("},
        ]
        for i, item in enumerate(self.items):
            if i > 0:
                messages.append({"type": "text", "text": ", "})
            messages.append(_printjson_item(item, self.player, state))
        messages.append({"type": "text", "text": ")"})
        return messages


@dataclasses.dataclass(frozen=True)
class HasAnyInstance(RuleInstance):
    items: Tuple[str, ...]

    def __hash__(self) -> int:
        return super().__hash__()

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.has_any(self.items, self.player)

    def deps(self) -> Dict[str, Set[int]]:
        return {item: {id(self)} for item in self.items}

    def serialize(self) -> str:
        return f"HasAny({', '.join(self.items)})"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        messages: List[JSONMessagePart] = [
            {"type": "text", "text": "Has "},
            {"type": "color", "color": "cyan", "text": "any"},
            {"type": "text", "text": " of ("},
        ]
        for i, item in enumerate(self.items):
            if i > 0:
                messages.append({"type": "text", "text": ", "})
            messages.append(_printjson_item(item, self.player, state))
        messages.append({"type": "text", "text": ")"})
        return messages


@dataclasses.dataclass(frozen=True)
class CanReachLocationInstance(RuleInstance):
    location: str
    parent_region: str
    cacheable: bool = dataclasses.field(repr=False, default=False, init=False)

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.can_reach_location(self.location, self.player)

    def indirect(self) -> "Tuple[RegionName, ...]":
        return (RegionName(self.parent_region),)

    def serialize(self) -> str:
        return f"CanReachLocation({self.location})"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        return [
            {"type": "text", "text": "Reached Location "},
            {"type": "location_name", "text": self.location, "player": self.player},
        ]


@dataclasses.dataclass(frozen=True)
class CanReachRegionInstance(RuleInstance):
    region: str
    cacheable: bool = dataclasses.field(repr=False, default=False, init=False)

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.can_reach_region(self.region, self.player)

    def indirect(self) -> "Tuple[RegionName, ...]":
        return (RegionName(self.region),)

    def serialize(self) -> str:
        return f"CanReachRegion({self.region})"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        return [
            {"type": "text", "text": "Reached Region "},
            {"type": "color", "color": "yellow", "text": self.region},
        ]


@dataclasses.dataclass(frozen=True)
class CanReachEntranceInstance(RuleInstance):
    entrance: str
    cacheable: bool = dataclasses.field(repr=False, default=False, init=False)

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.can_reach_entrance(self.entrance, self.player)

    def serialize(self) -> str:
        return f"CanReachEntrance({self.entrance})"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        return [
            {"type": "text", "text": "Reached Entrance "},
            {"type": "entrance_name", "text": self.entrance, "player": self.player},
        ]


@dataclasses.dataclass(frozen=True)
class HardLogicInstance(RuleInstance):
    child: RuleInstance

    def _evaluate(self, state: "CollectionState") -> bool:
        return state.has(Events.FAKE_OOL_ITEM.value, self.player)

    def deps(self) -> "Dict[str, Set[int]]":
        deps = self.child.deps()
        deps.setdefault(Events.FAKE_OOL_ITEM.value, set()).add(id(self))
        return deps

    def indirect(self) -> "Tuple[RegionName, ...]":
        return self.child.indirect()

    def serialize(self) -> str:
        return f"HardLogic[{self.child.serialize()}]"

    def explain(self, state: "CollectionState | None" = None) -> "List[JSONMessagePart]":
        messages: "list[JSONMessagePart]" = [
            {"type": "color", "color": "glitched", "text": "Hard Logic ["},
        ]
        messages.extend(self.child.explain(state))
        messages.append({"type": "color", "color": "glitched", "text": "]"})
        return messages
