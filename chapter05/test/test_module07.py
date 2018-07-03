import pytest




@pytest.fixture()
def fixture01(request):
    print("\nIn fixture...")

    # Run a block of code
    #   after the test with a fixture has run

    def fin():
        print("\nFinalized...")
    request.addfinalizer(fin)

@pytest.mark.usefixtures('fixture01')
def test_case01():
    print("\nI'm the test_case01")


@pytest.mark.usefixtures('fixture01')
def test_case02():
    print("\nI'm the test_case02")
