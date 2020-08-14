from unittest import TestCase
from ddt import ddt, data, file_data, unpack
from src.calc import Calc
import yaml


@ddt
class TestCalc(TestCase):

    def setUp(self) -> None:
        self.calc = Calc()

    @data(1, 5, 6)
    def test_demo(self, real):
        self.assertEqual(real, 5)

    @data((1, 1, 2),
          (1, 0, 1),
          (1, -1, 0),
          (1, 10000, 10001)
          )
    @unpack
    def test_add(self, a, b, c):
        result = self.calc.add(a, b)
        self.assertEqual(result, c)

# 参数方在yaml文件中
    @file_data("calc.yaml")
    def test_div(self, a, b, c):
        result = self.calc.div(a, b)
        self.assertEqual(result, c)

    def test_above(self):
        result = self.calc.above(1, 2)
        self.assertEqual(result, False)

        result = self.calc.above(2, 1)
        self.assertEqual(result, True)

        result = self.calc.above(1, 1)
        self.assertEqual(result, False)

        result = self.calc.above(1.1, 2.1)
        self.assertEqual(result, False)
