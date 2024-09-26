from is_even import is_even
import pytest

def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    assert is_even(-3) == False

def test_is_even_invalid_input():
    with pytest.raises(TypeError):
        is_even("not a number")

    with pytest.raises(TypeError):
        is_even(None)

    with pytest.raises(TypeError):
        is_even([2, 4, 6])
        is_even((2, 4, 6))
