from sum_positive import sum_positive
import pytest

def test_all_positive():
    assert sum_positive([1, 2, 3]) == 6

def test_empty():
    assert sum_positive([]) == 0

def test_negative_raises():
    with pytest.raises(ValueError):
        sum_positive([1, -2, 3])
