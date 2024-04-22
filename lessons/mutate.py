"""Mutating functions."""


__author__ = "730662932"


def manual_append(list: list[int], paper: int) -> None:
    """Taking a list and appending."""
    list.append(paper)


corn: list[int] = []
manual_append(corn, 1)
manual_append(corn, 3)
manual_append(corn, 5)
print(corn)


def double(list: list[int]) -> None:
    """Taking a list and multiplying by 2."""
    counter: int = 0
    while counter < len(list):
        val: int = list[counter] * 2
        list[counter] = val
        counter += 1


double(corn)
print(corn)