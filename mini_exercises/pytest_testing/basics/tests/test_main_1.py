from ..src.main_1 import add, divide
import pytest


def test_add():
    assert add(2, 3) == 5, "2 + 3 should be 5"
    assert add(1, 1) == 2, "1 + 1 should be 2"
    assert add(2, -3) == -1, "2 + (-3) should be -1"


def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
    assert divide(10, 5) == 2
    assert divide(10, 6) == 1.67
