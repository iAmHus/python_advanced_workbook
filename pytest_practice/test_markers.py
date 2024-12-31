import pytest

@pytest.mark.sanity_test
def test_01():
    assert type(3.5) == float

# Unconditional skip
@pytest.mark.skip
def test_02():
    assert 1 == 1


@pytest.mark.xfail
def test_xfail():
    x = 2/0

@pytest.mark.xfail(raises=Exception)
def test_xfail():
    x = 2/0
# @pytest.mark.skipif(condition=os)
# def test_03():
