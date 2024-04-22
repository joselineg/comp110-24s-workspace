"""Summing the elements of a list using different loops."""

__author__ = "730662932"


def w_sum(vals: list[float]) -> float:
    """Coding with a while loop."""
    sum = 0.0
    if (len(vals) == 0):
        return sum
    element: int = len(vals) - 1
    while (element >= 0):
        sum += vals[element]
        element -= 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Coding with a for in loop."""
    sum = 0.0
    for value in vals:
        sum += value
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Coding with a for in range loop."""
    sum = 0.0
    for elements in range(len(vals)):
        sum += vals[elements]
    return sum