import pytest
import time


def add(x, y):
    return x + y


def test_add():
    assert add(1, 2) == 3


def test_add2():
    print("I am 2")
    time.sleep(3)
    pytest.assume(add(1.2, 3.1) == 5.3)
    assert add(1, 2) == 3
