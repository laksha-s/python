from typing import Generic, TypeVar

_T = TypeVar("_T")

class TypeChecker(Generic[_T]):
    def __init__(self, *acceptable_types: _T): ...
    def CheckValue(self, proposed_value: _T) -> _T: ...

class TypeCheckerWithDefault(TypeChecker[_T]):
    def __init__(self, default_value: _T, *acceptable_types: _T): ...
    def DefaultValue(self) -> _T: ...
