import pytest


# Hmm.. Fixtures like this are far easy to understand!!
@pytest.fixture()
def fixture01():
    print("\nIn fixture01()...")

def test_case01(fixture01):
    print("\nIn test_case01()...")

