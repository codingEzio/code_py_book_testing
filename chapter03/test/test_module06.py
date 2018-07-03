import unittest


# You don't actually need the 'if ... unittest.main'
#   type "python -m unittest FILENAME -v" to do that

class TestCase07(unittest.TestCase):

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("\nIn test_case01()")
