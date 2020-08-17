import logging
import pytest
from src.calc import Calc
import yaml

logging.basicConfig(level=logging.DEBUG)


def setup_module():
    logging.info("整个module开始执行，login")


def teardown_module():
    logging.info("整个module执行完毕，logout")


class TestA:
    @pytest.mark.parametrize("a,b,c", [(1, 1, 2), (2, 2, 4)])
    def test01(self, a, b, c):
        logging.info("test01开始执行了")
        result = Calc().add(a, b)
        assert result == c

    @pytest.mark.parametrize("a,b,c", yaml.load(open("D:/test/PythonTest/testcase/calc2.yaml")))
    def test02(self, a, b, c):
        logging.info("test02开始执行了")
        result = Calc().div(a, b)
        assert result == c

    def test03(self):
        logging.info("test03开始执行了")

    @classmethod
    def teardown_class(cls):
        logging.info("TestA 的环境清理")


class TestB:
    def setup_method(self):
        logging.info("TestB的每个方法都有的初始化")

    def test04(self):
        logging.info("test04开始执行了")

    def test05(self):
        logging.info("test05开始执行了")

    def test06(self):
        logging.info("test06开始执行了")


class TestC:
    @pytest.mark.last
    def test07(self):
        logging.info("test07开始执行了")

    @pytest.mark.run(after="test09")
    def test08(self):
        logging.info("test08开始执行了")

    @pytest.mark.run(after="test06")
    def test09(self):
        logging.info("test09开始执行了")


if __name__ == '__main__':
    pass
