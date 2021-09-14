from abc import ABC
from typing import _UnionGenericAlias


class IFG(ABC):
    """
    Interface guard protects your interface and base class properties and their types.
    """

    def __init__(self, type_safe: bool = True):
        base_annotations = self.__class__.__base__.__dict__.get('__annotations__', {})
        for name_, type_ in base_annotations.items():
            assert hasattr(
                self, name_
            ), f'required attribute "{name_}" not present in "{self.__class__}"'
            if type_safe:
                assert self._super_is_instance(
                    name_, type_
                ), f'expected attribute "{name_}" to be "{type_}" not "{type(self.__getattribute__(name_))}"'

    def _super_is_instance(self, name_, type_):
        if type_.__class__ == _UnionGenericAlias:
            if any(
                list(
                    map(
                        lambda union_type_: self._super_is_instance(name_, union_type_),
                        type_.__args__,
                    )
                )
            ):
                return True
            else:
                return False
        if type_ == type(self.__getattribute__(name_)):
            return True
        else:
            return False