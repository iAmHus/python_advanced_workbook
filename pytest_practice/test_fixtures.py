
# Shared fixture defined in conftest.py
def test_shared_fixture(shared_fixture):
    assert 1 <= shared_fixture <= 5