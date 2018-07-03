import unittest


# Try something different (cmd args)
#   [-q]    display info briefly ( 简略"通过的", "未通过的"依如从前 )
#   [-f]    stop on first fail or error ( yep )
#   [-fv]   hmm.. "failsaft" plus "verbose"

class TestCase08(unittest.TestCase):

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("\nIn test_case1()")

    def test_case02(self):
        self.assertTrue("Python".isupper())
        print("\nIn test_case2()")

    def test_case03(self):
        self.assertTrue(True)
        print("\nIn test_case3()")
