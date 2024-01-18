from Lab3.src.Unit_test import calculator


def test_sum():
    result = calculator(3, 1, '+')
    assert result == 3


def test_sum1():
    result = calculator(3, 1, '+')
    assert result == 4


def test_minus():
    result = calculator(3, 1, '-')
    assert result == 2


def test_minus1():
    result = calculator(3, 1, '-')
    assert result == 7


def test_multy():
    result = calculator(3, 1, '*')
    assert result == 3


def test_multy1():
    result = calculator(2, 5, '*')
    assert result == 10


def test_devide():
    result = calculator(7, 1, '/')
    assert result == 7


def test_devide1():
    result = calculator(3, 1, '/')
    assert result == 3