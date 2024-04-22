"""Demonstrate Basic List Syntax"""

# Create an empty list
grocery_list: list[str] = list() # <- constructor
grocery_list: list[str]= [] # <- literal 
print("Empty list")
print(grocery_list)


# Add to a list
grocery_list.append("frosted flakes")
grocery_list.append("milk")
grocery_list.append("pizza")
print("After adding things:")
print(grocery_list)

# Create a list with objects in it
grocery_list2: list[str] = ["frosted flakes", "milk", "pizza"]
print("Already populated lsit: ")
print(grocery_list2)

grocery_list2.append("whipped cream")
print("Add another thing:")
print(grocery_list2)


# Indexing 
print("Printing one item:")
print(grocery_list[0])


# Modifying 
x: list[str]= ["c", "a", "r","s"]
x[2]= "t"
print(x)


grocery_list[0] = "cinnamon toast crunch"
print("Modifying: ")
print(grocery_list)


# Length of a list
print("Length:")
print(len(grocery_list))

# Remove an item
grocery_list.pop(1)
print("Remove an item:")
print(grocery_list)

grocery_list.remove("pizza")
print(grocery_list)


# Function name: display 
# Parameter: list[str]
# Return Nothing!
# Print out the list!

def display(list: list[str]) -> None:
    print(list)

tennis_shoes: list[str] = list()
tennis_shoes.append("vans")
tennis_shoes.append("jordans")
tennis_shoes.append("nike")
display(tennis_shoes)

def corn(list: list[int]) -> None: 
    print(list)

favorite_numbers: list[int] = [7,4,3]
corn(favorite_numbers)


# Create a list!
# Name: create
# Parameters: str and str
# RV: list[str]
# Put both parameters into list and return that list 

def create(list_item: str, list_item2: str) -> list[str]:
    corn: list[str] =  [list_item, list_item2]
    return(corn)


x = create("dr.pepper", "cookies")
print(x)


def create(word1: str, word2: str) -> list[str]:
    new_list: list[str] = [word1, word2]
    return new_list

x: list[str]