"""List Utility Functions!"""

__author__ = "730662932" 


def all(lists: list[int], number: int) -> bool:
    """Establishing an all function."""
    if not lists:
        return False
    for list in lists:
        if list != number:
            return False
    return True


def max(lists: list[int]) -> int:
    """Establishing a max function."""
    if not lists:
        raise ValueError("max() arg is an empty List")
    max_num = lists[0]
    for num in lists:
        if num > max_num:
            max_num = num
    return max_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Establishing an equal function."""
    if len(list_1) != len(list_2):
        return False
    for idx in range(len(list_1)):
        if list_1[idx] != list_2[idx]:
            return False
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Establishing an extended function."""
    list_1.extend(list_2)