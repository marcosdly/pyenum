"""Define the allowed member creation mechanisms"""

from dataclasses import dataclass, field
from typing import Any

class ImplicitValue: pass

@dataclass(init=True)
class Member:
    name: str = field(init=False)
    value: Any = field(init=True, default=ImplicitValue)

    def __init_subclass__(cls) -> None:
        raise SyntaxError("The member implementation class cannot be subclassed. All means of member creation must constrain their functionality to this class' implementation (a.k.a. return this class).")