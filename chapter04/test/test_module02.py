from mypackage.mymathlib import *

# You can test like just like unittest:
#   nosetests test.test_module02 -v
#   nosetests test.test_module02:TestClass01.test_case01 -v

# Also, you can test them all at once
#   nosetests test/* -v     (hmm..)


class TestClass01:
    def test_case01(self):
        print("In test_case01()")
        assert mymathlib().add(2, 5) == 7
