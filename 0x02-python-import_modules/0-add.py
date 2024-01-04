#!/usr/bin/python3
if __name__ == "main":
    from add_0 import add
    """My addition function

    Args:
        a: first integer
        b: second integer
    Returns:
        The return value. a + b
    """
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
