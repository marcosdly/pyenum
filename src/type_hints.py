"""Type-hint classes for LSP recognition. Classes like this can be seen
throughout the code base to alert the LSP about objects that are dinamically
declared or/and depend on context to exist. Some of them can actually be functional,
but their ultimate purpose is typing."""

from dataclasses import dataclass, field
from typing import Callable, Any

@dataclass(init=True, frozen=False)
class MatchInfo:
    active: bool = field(init=False, default=False)
    already: set = field(init=False, default_factory=set)
    # not_yet: set = field(default=set())

@dataclass(init=True, frozen=True)
class MetaInfo:
    members: dict[str, Any]
    match: MatchInfo

@dataclass(init=False, frozen=True)
class BaseEnumTyping:
    meta: MetaInfo

# Has important functionality
# class MatchEnum(metaclass=MatchMeta):
#     pass