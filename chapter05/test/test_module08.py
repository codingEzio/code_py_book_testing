import pytest


# Plus,
#   you can specify the scope of the fixtures
#       @pytest.fixture(scope="class")
#   "function"      run it after every single test
#   "class"         run in each class of tests
#   "module"        run at start/end of the file (e.g. db connection)
#   "session"       run it at the first test and run the finalizer after the latest

@pytest.fixture()
def fixture01(request):
    # Check the info of the fixture on the "requested" object
    print("\nIn fixture...")
    print("Fixture Scope\t:\t" + str(request.scope))
    print("Function Name\t:\t" + str(request.function.__name__))
    print("Class Name\t:\t" + str(request.cls))
    print("Module Name\t:\t" + str(request.module.__name__))
    print("File Path\t:\t" + str(request.fspath))


@pytest.mark.usefixtures('fixture01')
def test_case01():
    print("\nI'm the test_case01")
