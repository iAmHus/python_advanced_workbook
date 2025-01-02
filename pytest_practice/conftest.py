import random

import pytest


# using conftest.py for shared fixtures

@pytest.fixture(name="shared_fixture")
def shared_fixture():
    yield random.randint(1,5)