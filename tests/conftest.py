import pytest
import time

@pytest.fixture(autouse=True)
def test_interval():
    yield
    time.sleep(1)