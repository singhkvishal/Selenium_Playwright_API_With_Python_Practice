import math
import pytest
@pytest.mark.Calculation
def test_sqrt():
    print("*************************Test SQRT******************8888")
    num = 25
    assert math.sqrt(num) == 5
@pytest.mark.Calculation
def test_square():
    num = 7
    assert 7*7 == 49
def test_equality():
    assert 10 == 10