"""Exercise 06 - Dictionary Unit Test."""

__author__ = "730662932" 


from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance
import pytest


def test_invert_empty() -> None:
    """Using an empty dict for invert."""
    assert invert([]) == {}


def test_invert() -> None:
    """Using test invert to return values."""
    test_dictionary: dict[str, str] = {'bird': 'lizard', 'banana': 'kiwi', 'star': 'planet'}
    assert invert(test_dictionary) == {'lizard': 'bird', 'kiwi': 'banana', 'planet': 'star'}


def test_invert_one() -> None:
    """Invert function does not function with the same keys."""
    dictionary_one = {'a': 'b', 'y': 'b'}
    with pytest.raises(KeyError):
        invert(dictionary_one)


def test_favorite_color_empty() -> None:
    """Testing favorite color with an empty list."""
    test_empty: dict[str, str] = {}
    assert favorite_color(test_empty) == ""


def test_favorite_color() -> None:
    """The function favorite color must return a favorite color."""
    test_dictionary: dict[str, str] = {'kathy': 'purple', 'joseline': 'pink', 'zohat': 'pink'}
    assert favorite_color(test_dictionary) == 'pink'


def test_other_colors() -> None:
    """Adding more names and colors to return a favorite color."""
    test_dictionary: dict[str, str] = {'jasmin': 'black', 'maria': 'black', 'rossy': 'blue'}
    assert favorite_color(test_dictionary) == 'black'


def test_count_empty() -> None:
    """Testing count with an empty list."""
    test_dictionary: dict[str, int] = []
    assert count(test_dictionary) == {}


def test_count() -> None:
    """Testing count with a list."""
    test_list: list[str] = ['pink', 'black']
    assert count(test_list) == {'pink': 1, 'black': 1}


def test_count_one() -> None:
    """Testing count function with elements."""
    assert count(['black', 'pink', 'purple', 'black', 'pink']) == {'black': 2, 'pink': 2, 'purple': 1}


def test_alphabetizer_empty() -> None:
    """Testing alphabetizer with an empty list."""
    list_one: list[str] = []
    assert alphabetizer(list_one) == {}


def test_alphabetizer() -> None:
    """Testing alphabetizer with a list of words."""
    list_one: list[str] = ['kathy', 'joseline', 'zohat']
    expected = {'k': ['kathy'], 'j': ['joseline'], 'z': ['zohat']}
    assert alphabetizer(list_one) == expected


def test_alphabetizer_one() -> None:
    """Testing alphabetizer with the  same names."""
    list_one: list[str] = ['joseline', 'zohat', 'kathy', 'maria', 'ricky']
    expected = {'j': ['joseline'], 'z': ['zohat'], 'k': ['kathy'], 'm': ['maria'], 'r': ['ricky']}
    assert alphabetizer(list_one) == expected


def test_update_attendance_empty() -> None:
    """Testing updated attendance with an empty list."""
    test_updates: dict[str, list[str]] = {}
    assert update_attendance(test_updates, 'Monday', 'Joseline') == {'Monday': ['Joseline']}


def test_update_attendance() -> None:
    """Testing update attendance with the same attendance."""
    test_updates: dict[str, list[str]] = {'Tuesday': ['Joseline', 'Zohat'], 'Wednesday': ['Kathy']}
    assert update_attendance(test_updates, 'Tuesday', 'Ricky') == {'Tuesday': ['Joseline', 'Zohat', 'Ricky'], 'Wednesday': ['Kathy']}


def test_update_attendance_one() -> None:
    """Testing update attendance one with the same attendance."""
    test_updates: dict[str, list[str]] = {'Tuesday': ['Joseline', 'Zohat'], 'Wednesday': ['Kathy']}
    assert update_attendance(test_updates, 'Wednesday', 'Ricky') == {'Tuesday': ['Joseline', 'Zohat'], 'Wednesday': ['Kathy', 'Ricky']}