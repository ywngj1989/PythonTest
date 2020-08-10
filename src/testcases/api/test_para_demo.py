import pytest
from myapp import add


# 一次可以跑多种场景的用例
@pytest.mark.parametrize("x,y", [
    (3+5, 8),
    (2+4, 6),
    (6*9, 42)
])
def test_add_by_paras(x, y):
    assert add.add_method(x, y) == (x + y)
