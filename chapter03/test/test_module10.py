import unittest


conventions_for_unittest = """ --
-- all the test files should be importable from the top-level of the project
-- execute "discovery" from the test directory  ( find all -> test all )
-- the filenames should be like this 'test*.py' """

# Hey! See what I got:
#   self.id()                   check out what function are you testing
#   self.ShortDescription()     the comments on that function


class TestClass11(unittest.TestCase):

    def test_case01(self):
        """This is a test method..."""
        print("\nIn test_case01()")
        print("id -- ", self.id())
        print("sd -- ", self.shortDescription())
