import pytest


@pytest.fixture()
def fixture01():
    print("\nIn fixture01()...")


# It'll return the same result 
#   whether u have the decorator or not  ( maybe for readability? )
@pytest.mark.usefixtures("fixture01")
def test_case01(fixture01):
    print("\nIn test_case01()...")