import pytest
from src.soma import soma

def test_soma():
    assert soma(1, 2) == 3
    assert soma(0, 0) == 0
    assert soma(-1, 1) == 0
    assert soma(3, 5) == 8
