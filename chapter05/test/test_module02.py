
# run all/single 
#   py.test -v PACKAGE     
#   py.test -v PACKAGE/FILE

# run specific one
#   py.test -v PACKAGE/FILE::CLASS
#   py.test -v PACKAGE/FILE::CLASS::METHOD


class TestClass01:

    def test_case01(self):
        assert 'python'.upper() == 'PYTHON'

    def test_case02(self):
        assert 'PYTHON'.lower() == 'python'