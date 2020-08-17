import pytest


@pytest.mark.parametrize("test_input,excepted", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, excepted):
    assert eval(test_input) == excepted