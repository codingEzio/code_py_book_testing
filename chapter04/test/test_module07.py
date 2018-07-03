from nose.tools import raises


# If you use the "@raise" decorator,
#   the error you raised in your own test case
#   must match at least one of them that you put into the decorator

# What if.. NOT?
#   well, FAILED apparently....


@raises(TypeError, ValueError)
def test_case01():
    raise TypeError("This test passes")


@raises(ValueError)
def test_case02():
    raise TypeError("Hmm, it doesn't match!!")


@raises(Exception)
def test_case03():
    pass
