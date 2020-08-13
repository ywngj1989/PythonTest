from unittest import TestCase
from src.calc import Calc


class TestCalc(TestCase):
    def test_add(self):
        calc = Calc()
        result = calc.add(1, 1)
        #assert result == 2
        self.assertEqual(result, 2)

        result = calc.add(1, 0)
        #assert result == 1
        self.assertEqual(result, 1)

        result = calc.add(1, -1)
        #assert result == 0
        self.assertEqual(result, 0)

        result = calc.add(1, 10000)
        #assert result == 10001
        self.assertEqual(result, 10001)

    def test_div(self):
        calc = Calc()
        result = calc.div(2, 1)
        self.assertEqual(2, result)

        result = calc.div(1, 2)
        self.assertEqual(result, 0.5)

        result = calc.div(2, 0)
        self.assertEqual(result, None)

    def test_above(self):
        calc = Calc()

        result = calc.above(1, 2)
        self.assertEqual(result, False)

        result = calc.above(2, 1)
        self.assertEqual(result, True)

        result = calc.above(1, 1)
        self.assertEqual(result, False)
