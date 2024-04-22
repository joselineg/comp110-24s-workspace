"""Writing a Recursive Function - CQ07."""


__author__ = "730662932"


def f(n: int, k: int) -> int:
    """Defining a Recursive Definition."""
    if n == 0:  # base case
        return 0 
    elif n % 1 == 0:  # recursive rule for even n
        return k * n
    else:  # recursive rule for odd n
        return k * (n - 1)