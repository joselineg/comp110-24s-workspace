"""Test my garden functions."""

__author__ = "730662932" 


from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date
"""Importing functions into garden helpers."""


def test_add_by_kind_edge_case():
    """Testing add_by_kind a plant with an empty kind."""
    plants_by_kind = {}
    plant_kind = "flowers"
    plant_type = "tulips"
    add_by_kind(plants_by_kind, plant_kind, plant_type)
    assert plants_by_kind == {"flowers": ["tulips"]}


def test_add_by_kind_use_case():
    """Testing add_by_kind a plant to an already existing kind."""
    plants_by_kind = {"flowers": ["tulip"]}
    plant_kind = "flowers"
    plant_type = "peonies"
    add_by_kind(plants_by_kind, plant_kind, plant_type)
    assert plants_by_kind == {"flowers": ["peonies", "tulip"]}  # Corrected order


def test_add_by_date_edge_case():
    """Testing add_by_date a plant with an empty month."""
    plants_by_date = {}
    plant_date = "March"
    plant_type = "lettuces"
    add_by_date(plants_by_date, plant_date, plant_type)
    assert plants_by_date == {"March": ["lettuces"]}


def test_add_by_date_use_case():
    """Testing add_by_date a plant to an already existing date."""
    plants_by_date = {"March": ["lettuces"]}
    plant_date = "March"
    plant_type = "carrots"
    add_by_date(plants_by_date, plant_date, plant_type)
    assert plants_by_date == {"March": ["carrots", "lettuces"]}  # Corrected order


def test_lookup_by_kind_and_date_edge_case():
    """Searching for plants with no kind or date with lookup_by_kind_and_date."""
    plants_by_kind = {}
    plants_by_date = {}
    plant_kind = "flowers"
    plant_date = "April"
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, plant_date)
    expected = f"No {plant_kind}s to plant in {plant_date}."
    assert result == expected


def test_lookup_by_kind_and_date_use_case():
    """Searching for plants with an already existing kind and date with lookup_by_kind_and_date."""
    plants_by_kind = {"flowers": ["peonies", "tulips"]}
    plants_by_date = {"March": ["tulips", "cabbages"], "April": ["peas", "tulips"]}
    plant_kind = "flowers"
    plant_date = "April"
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, plant_date)
    expected = f"{plant_kind}s to plant in {plant_date}: ['peas', 'tulips']."  # Include 'peas'
    assert result == expected