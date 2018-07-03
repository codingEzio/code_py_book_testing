
all = [
    "test_module01",
    "test_module02",
    "test_module03",
    "test_module04",
    "nose_htmloutput",
]


# This is a package-level fixtures (run before/after ...)
# It means that
#   all tests in this dir include these, have a look:
#       In setUpPackage()...
#           ...
#           ...
#       In tearDownPackage()...

def setUpPackage():
    print("In setUpPackage()...")


def tearDownPackage():
    print("In tearDownPackage()...")
