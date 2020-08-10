import pytest
import logging
from myapp import add


def setup_module():
    print("login")


def teardown_module():
    print("整个module 完成清理环境")


class TestA:
    @classmethod
    def teardown_class(cls):
        print("")

    def test_one(self):
        print("我是test_one")

    def test_two(self):
        print("我是test_two")

    def test_three(self):
        print("我是test_three")

    @classmethod
    def teardown_class(cls):
        print("TestA的 teardown")


class TestB:
    def setup(self):
        print("TestB 的 每个方法执行之前调用")

    def test_four(self):
        print("我是test_four")

    def test_five(self):
        print("我是test_five")

    @pytest.mark.parametrize("x,y", [
        (3 + 5, 8),
        (2 + 4, 6),
        (6 * 9, 42)
    ])
    def test_six(self, x, y):
        print("我是test_six")
        assert add.add_method(x, y) == (x + y)


class TestC:
    @pytest.mark.run('three')
    def test_seven(self):
        print("我是test_seven")

    @pytest.mark.run('first')
    def test_eight(self):
        print("我是test_eight")

    @pytest.mark.run('second')
    def test_nine(self):
        print("我是test_nine")


if __name__ == '__main__':
    pytest.main(['-s', 'test_pytest_homework.py'])
