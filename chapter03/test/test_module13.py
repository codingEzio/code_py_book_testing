import unittest


class TestClass14(unittest.TestCase):
    def test_case01(self):
        # this one was different from the "self.fail()"
        raise Exception
