from nose.tools import with_setup


def setUpModule():
    """called once, before anything else in this module"""
    print("\nIn setUpModule()...")


def tearDownModule():
    """called once, after everything else in this module"""
    print("\nIn tearDownModule()...")


def setup_function():
    """setup_function(): use it with @with_setup() decorator"""
    print("\nsetup_function()...")


def teardown_function():
    """teardown_function(): use it with @with_setup() decorator"""
    print("\nteardown_function()...")


# The 'case01' and 'case02' are just normal functions
#   ( the func bound to a class was called 'method' )

def test_case01():
    print("In test_case01()...")


def test_case02():
    print("In test_case02()...")


# by using the two decorators, you can 
#   使测试用例 在测试之前执行xxx  ( 如 setup_function )
#   使在测试完成后 执行xxx       ( 如 teardown_function )
@with_setup(setup_function, teardown_function)
def test_case03():
    print("In test_case03()...")
