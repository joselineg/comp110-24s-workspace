"""Some functions for my garden plan!"""

__author__ = "730662932" 


plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}

plants: str = "apple"
plant_kind: str = "fruit"

# Function name: add_by_kind
# Parameters: dict[str, list[str]], str, str
# Return Type: None


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind: str, plant: str) -> None:
    """Add_by_kind with types of plants."""
    if plant_kind in plants_by_kind:
        plants_by_kind[plant_kind].append(plant)
    else:
        plants_by_kind[plant_kind] = []
        plants_by_kind[plant_kind].append(plant)


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str,) -> None:
    """Add_by_kind with dates of plants."""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = []
        plants_by_date[month].append(plant)

# Function name: lookup_by_kind_and_date
# Parameters: dict[str, list[str]], dict[str, list[str]], str, str
# Return Type: str
       

def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
    """Lookup_by_kind with both date and flower."""
    if plant_kind not in plants_by_kind or month not in plants_by_date:
        return f"No {plant_kind}s to plant in {month}"
    kind_list: list[str] = plants_by_kind[plant_kind]
    month_list: list[str] = plants_by_date[month]
    combined_list: list[str] = []
    for plant in kind_list:
        if plant in month_list:
            combined_list.append(plant)
    if combined_list:
        return f"{plant_kind}s to plant in {month}: {combined_list}"
    else:
        return f"No {plant_kind}s to plant in {month}"