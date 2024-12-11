import pytest
π
@pytest.mark.sanity_test
def test_01():
    assert type(3.5) == float

# Unconditional skip
@pytest.mark.skip
def test_02():
    assert 1 == 1

# @pytest.mark.skipif(condition=os)
# def test_03():
