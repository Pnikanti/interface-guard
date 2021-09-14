from IFG import IFG
from typing import Union


class TypeSafeBaseClassExample(IFG):
    """
    Example base class using InterfaceGuard base class.
    """

    my_str_property: str
    my_union_property: Union[list, tuple]

    def __init__(self):
        super().__init__()
        print("type safe base class instantiated")


class TypeSafeDerivedClassExample(TypeSafeBaseClassExample):
    def __init__(self):
        self.my_str_property = "string"
        self.my_union_property = {
            "key": "value"
        }  # throws error because expected type is list or type, not dict
        super().__init__()
        print("type safe derived class instantiated")


class NonTypeSafeBaseClassExample(IFG):
    """
    Example base class using InterfaceGuard base class.
    """

    my_str_property: str
    my_union_property: Union[list, tuple]

    def __init__(self):
        super().__init__(type_safe=False)
        print("non type safe base class instantiated")


class NonTypeSafeDerivedClassExample(NonTypeSafeBaseClassExample):
    def __init__(self):
        self.my_str_property = "string"
        self.my_union_property = {"key": "value"}  # does not throw error
        super().__init__()
        print("non type safe derived class instantiated")


def main():
    x = NonTypeSafeDerivedClassExample()
    y = TypeSafeDerivedClassExample()


if __name__ == '__main__':
    main()