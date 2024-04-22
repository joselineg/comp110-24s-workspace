"""EX05 - Dictionary Utility Functions."""

__author__ = "730669232"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Defining invert."""
    b: dict[str, str] = {}
    for keys in a:
        if a[keys] in b:
            raise KeyError("error in invert!")
        else:
            b[a[keys]] = keys
    return b


def favorite_color(dictionary: dict[str, str]) -> str:
    """Defining favorite colors."""
    d: dict[str, int] = {}
    for key in dictionary:
        if dictionary[key] not in d:
            d[dictionary[key]] = 1
        else:
            d[dictionary[key]] += 1
    color: str = ""
    favorite_number: int = 0
    for key in d:
        if d[key] > favorite_number:
            color = key
        favorite_number = d[key] 
    return color


def count(a: list[str]) -> dict[str, int]:
    """Defining count."""
    d: dict[str, int] = {}
    for counter in a:
        if counter in d:
            d[counter] += 1
        else:
            d[counter] = 1
    return d


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Defining alphabetizer."""
    d: dict[str, list[str]] = {}
    for word in words:
        first: str = word[0].lower()
        if first in d:
            d[first].append(word)
        else:
            d[first] = [word]
    return d


def update_attendance(a: dict[str, list[str]], b: str, c: str) -> None:
    """Updating attendance."""
    if b in a:
        if c not in a[b]:
            a[b].append(c)
    else:
        a[b] = [c]