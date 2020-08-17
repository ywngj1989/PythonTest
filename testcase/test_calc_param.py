from src.calc import Calc
import pytest
import json
import yaml
"""
使用pytest参数化
"""


class TestCalc:
    def setup(self) -> None:
        self.calc = Calc()

    @pytest.mark.parametrize("a, b, c", [
        (1, 1, 2),
        (1, 0, 1),
        (1, -1, 0),
        (1, 1000, 1001)
    ])
    def test_add(self, a, b, c):
        result = self.calc.add(a, b)
        assert result == c

# 参数放在yaml/json文件中
    # @pytest.mark.parametrize("a,b,c", json.load(open("calc.json")))
    @pytest.mark.parametrize("a,b,c", yaml.load(open("calc2.yaml")))
    def test_div(self, a, b, c):
        result = self.calc.div(a, b)
        assert result == c
