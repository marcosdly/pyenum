from typing import Iterable, Union


class UnhandledEnumCasesError(Exception):
    def __init__(self, enum_name: str, unhandled_cases: Union[set, Iterable]) -> None:
        super().__init__(f"{len(unhandled_cases)} cases of '{enum_name}' were not handled: {list(unhandled_cases)}")