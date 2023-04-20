import pytest

from HW14.human import Human


@pytest.fixture(scope="module")
def human():
    yield Human("Eva", 25, "female")


@pytest.fixture(scope="module")
def old_human():
    yield Human("Adam", 100, "male")


@pytest.fixture(scope="module")
def non_human():
    yield Human("Gera", 40, "it")

