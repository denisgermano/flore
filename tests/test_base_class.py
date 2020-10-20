from flore.libraries.base import Base
from unittest.mock import patch


@patch.multiple(Base, __abstractmethods__=set())
def test_abstract_base_class():
    b = Base()

    try:
        b.open()
    except AttributeError as e:
        assert str(e) == "you can't use the abstract method"

    try:
        b.create()
    except AttributeError as e:
        assert str(e) == "you can't use the abstract method"
