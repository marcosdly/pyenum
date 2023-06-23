from typing import Any
from meta import EnumMeta, MatchMeta
from contextlib import contextmanager
from copy import deepcopy
from exceptions import UnhandledEnumCasesError

# Typing and more maintainable definition
class MatchEnum(metaclass=MatchMeta):
    pass

class Enum(metaclass=EnumMeta):
    @classmethod
    @contextmanager
    def match(cls) -> MatchEnum:
        enum = type(f"Match[{cls.__name__}]", (MatchEnum,), cls.meta.members)
        try: yield enum
        except: raise
        else:
            if not enum.all():
                raise UnhandledEnumCasesError(cls.__name__, enum.not_yet())