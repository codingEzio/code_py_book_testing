"""
Sample doctest test module...
test_module02
"""

# Words:
#   the output should be clean as hell ( 2*3? only 6 )
#   indentation COUNTS
#   type "python3 -m doctest -v FILENAME" to test

def mul(a, b):
    """
    >>> mul(2,3)
    6
        
    >>> mul('a',2)
    'aa'
    """
    return a*b


def add(a, b):
    """
    >>> add(2,3)
    5

    >>> add('a','b')
    'ab'
    """
    return a+b
