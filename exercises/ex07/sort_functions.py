"""Functions that implement sorting algorithms."""

__author__ = "730992632"


from random import randint


MAX_VAL = 1000000


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm."""
    n = len(x)
    for i in range(1, n):
        current_value = x[i]
        j = i - 1
        while j >= 0 and x[j] > current_value:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = current_value
    """Insert into an already sorted list."""

def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm."""
    n = len(x)
    for i in range(n):
        min_index = i
        for s in range(i +1, n):
            if x[s] < x[min_index]:
                min_index = s
        x[i], x[min_index] = x[min_index], x[i]
    """Find the minimum and swap them."""
    