import pytest
from main import cal

@pytest.mark.parametrize("_input, result", [
    ("1+2/2*50!#+(16^(1/2)-5!+4!)", -37.0),
    ("((15 * ~2) / (3^2+1)) + 4! % 135#", 3.0),
    ("(2^3 * ~5) + (10 / 32#) - 7", -45.0),
    ("((((~-3!!^~-3!)#/5) ^ 100)#!#)", 65.0)
])
def test_mytest(_input, result):
    assert cal(_input) == result