import unittest

# The test fixtures and their implementation
#   is the key feature in any test automation library.
#   It's the major advantage over the static doctest.

# Hey! You can also test them seperately (Damn!)
#   python -m unittest -v test_module05
#   python -m unittest -v test_module05.TestClass06
#   python -m unittest -v test_module05.TestClass06.test_case01

# See more by typing "python -m unittest -h"


def setUpModule():
    """called once, before anything else in this module"""
    print("In setUpModule()...")


def tearDownModule():
    """called once, after everything else in this module"""
    print("In tearDownModule()...")


class TestClass06(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """called once, before any test"""
        print("In setUpClass()...")

    @classmethod
    def tearDownClass(cls):
        """called once, after all tests, if setUpClass successful"""
        print("In tearDownClass()...")

    def setUp(self):
        """called multiple times, before every test method"""
        print("\nIn setUp()")

    def tearDown(self):
        """called multiple times, after every test method"""
        print("In tearDown()")

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("In test_case01()")

    def test_case02(self):
        self.assertTrue("python".isupper())
        print("In test_case02()")


if __name__ == "__main__":
    unittest.main()
