import pytest
from calculate.calculator_program import calculate


def test_addition():
    assert calculate(2, 3, '+') == 5


def test_division():
    assert calculate(6, 2, '/') == 3


def test_subtraction():
    assert calculate(10, 4, '-') == 6


def test_multiplication():
    assert calculate(4, 3, '*') == 12


def test_unknown_operation():
    with pytest.raises(ValueError):
        calculate(5, 5, '%')


def test_zero_division():
    with pytest.raises(ValueError):
        calculate(8, 0, '/')