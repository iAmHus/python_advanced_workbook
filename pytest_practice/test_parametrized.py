import pytest

@pytest.mark.parametrize("input_expected", [25,30,50,70])
def test_limit(input_expected):
    assert input_expected < 90

@pytest.mark.parametrize(argnames="val1,val2",
                         argvalues = [(25,30),(50,70)])
def test_two_params(val1, val2):
    assert val1 < val2

