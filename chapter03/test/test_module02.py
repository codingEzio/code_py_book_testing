import unittest
import inspect


# The test methods ran in alphabetical order
#   and all the test classes 
#     are executed one by one in alphabetical order as well

class TestClass02(unittest.TestCase):

    def test_case04(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])

    def test_case01(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
