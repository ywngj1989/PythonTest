import logging
import pytest

"""
1、用例顺序
setup_module
setup_class
setup_method
teardown_method
teardown_class
teardown_module
2、使用pytest-order控制用例之间的顺序
"""
logging.basicConfig(level=logging.DEBUG)


# 模块出初始化之前执行
def setup_module():
    logging.info("setup_module")


# 模块初始化之后执行
def teardown_module():
    logging.info("teardown_module")


class TestPytestObject2:
    def test_three(self):
        assert 5 == 6

    def test_four(self):
        assert {"a": 1, "b": "sss"} == {"a": 2, "b": "ss"}


class TestPytestObject:
    # 类初始化之前执行
    @classmethod
    def setup_class(cls):
        logging.info("setup_class")

    def setup_method(self):
        logging.info("setup_method")

    def setup_function(self):
        logging.info("setup_function")

    def setup(self):
        logging.info("setup")

    @pytest.mark.run(order=2)
    # @pytest.mark.run(after="one")
    def test_two(self):
        assert 1 == 2

    @pytest.mark.run(order=1)
    def test_one(self):
        assert True == False

    def teardown(self):
        logging.info("teardown")

    def teardown_method(self):
        logging.info("teardown_method")

    def teardown_function(self):
        logging.info("teardown_function")

    # 类初始化之后执行
    @classmethod
    def teardown_class(cls):
        logging.info("teardown_class")