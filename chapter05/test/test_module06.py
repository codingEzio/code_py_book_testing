import pytest


@pytest.fixture()
def fixture01():
    print("\nIn fixture01()...")


# Every method in this class will be 'influenced'
#   that means
#       "In fixture01()...  ...case1 "
#       "In fixture01()...  ...case2 "
@pytest.mark.usefixtures('fixture01')
class TestClass03:
    def test_case01(self):
        print("I'm the test_case01")

    def test_case02(self):
        print("I'm the test_case02")
