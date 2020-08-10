# ! /usr/bin/env python
# coding=utf-8
from myapp import add


def test_add():
    assert add.add_method(10, 2) == 12


def test_add2():
    assert add.add_method(1, 2) == 3
