import pytest
from src.math_utils import add, subtract, multiply

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (5, 3, 8),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 1, 0),
    (0, 5, -5),
])
def test_subtraction(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (4, 0, 0),
    (-2, 3, -6),
])
def test_multiplication(a, b, expected):
    assert multiply(a, b) == expected


def test_string_equality():
    assert "hello" == "hello"


def test_list_contents():
    fruits = ["apple", "banana", "cherry"]
    assert "banana" in fruits
    assert len(fruits) == 3
