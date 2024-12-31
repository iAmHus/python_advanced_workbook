import pytest

@pytest.mark.parametrize("input_expected", [25,30,50,70])
def test_limit(input_expected):
    assert input_expected < 90