import logging
import pytest
'''
1、用例顺序
setup_module
setup_class
setup_method
teardown_method
teardown_class
teardown_module
2、pytest-ording功能：
指定方法执行顺序
'''


def setup_module():
    logging.info("setup_module")


def teardown_module():
    logging.info("tear_module")


class TestPytestObject2:
    def test_three(self):
        assert [1, 2] == [1, 3]

    def test_four(self):
        assert {"a": 1, "b": "sss"} == {"a": 2, "b": "s"}


class TestPytestObject:
    @classmethod
    def setup_class(cls):
       logging.basicConfig(level=logging.DEBUG)

    #@pytest.mark.run(order=2)
    @pytest.mark.run(after='test_one')
    @pytest.mark.run('second')
    def test_two(self):
        assert 1 == 2

   # @pytest.mark.run(order=1)
    @pytest.mark.run(before='test_two')
    @pytest.mark.run('first')
    def test_one(self):
        assert 1 == 1

    @classmethod
    def teardown_class(cls):
        logging.info("testdown")

