from myapp import add
import random
import pytest


def test_rerun_add():
    assert add.add_method(2, 3) == random.randint(1, 10)
