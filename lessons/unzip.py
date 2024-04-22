"""Splitting a dictionary into two lists."""

__author__ = "730669232"


def get_keys(list_1: dict[str, int]) -> list[str]:
    """Listing keys."""
    return list(list_1.keys())


def get_values(list_1: dict[str, int]) -> list[int]:
    """Listing values."""
    return list(list_1.values())