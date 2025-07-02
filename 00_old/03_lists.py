"""
This script demonstrates:
1. Creating and initializing lists.
2. Accessing elements using indexing and slicing.
3. Common list methods (append, insert, remove, pop, extend, sort, reverse, etc.).
4. Iterating over lists.
5. List comprehensions for concise list creation.
6. Nested lists.

How to run:
    python 03_lists.py
"""

# ------------------------------------------------------------------------------
# SECTION 1: Creating and Initializing Lists
# ------------------------------------------------------------------------------
print("=== SECTION 1: CREATING AND INITIALIZING LISTS ===")

# Creating a list using square brackets []
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# Creating an empty list and then populating it
numbers = []  # empty list
for i in range(5):
    numbers.append(i * 2)  # Appending multiples of 2
print("Numbers list after appending:", numbers)

# Lists can contain mixed data types
mixed_list = [1, "two", 3.0, True]
print("Mixed list:", mixed_list)

print()

# ------------------------------------------------------------------------------
# SECTION 2: Indexing and Slicing
# ------------------------------------------------------------------------------
print("=== SECTION 2: INDEXING AND SLICING ===")

sample_list = ["a", "b", "c", "d", "e"]
print("Sample list:", sample_list)

# Indexing: Access individual elements
print("First element (index 0):", sample_list[0])
print("Last element (index -1):", sample_list[-1])

# Slicing: Get a sub-list (from index 1 to 3, not including index 4)
sub_list = sample_list[1:4]
print("Sub-list from index 1 to 3:", sub_list)

# Slicing with step: Every 2nd element
print("Every 2nd element:", sample_list[::2])

print()

# ------------------------------------------------------------------------------
# SECTION 3: List Methods
# ------------------------------------------------------------------------------
print("=== SECTION 3: COMMON LIST METHODS ===")

my_list = [10, 20, 30]
print("Original list:", my_list)

# append(): Adds an element at the end of the list.
my_list.append(40)
print("After append(40):", my_list)

# insert(): Inserts an element at a specified index.
my_list.insert(1, 15)  # Insert 15 at index 1
print("After insert(1, 15):", my_list)

# extend(): Extends the list by appending elements from another list.
my_list.extend([50, 60])
print("After extend([50, 60]):", my_list)

# remove(): Removes the first occurrence of a value.
my_list.remove(20)
print("After remove(20):", my_list)

# pop(): Removes and returns the element at a given index (default last).
popped_element = my_list.pop()  # removes the last element
print("After pop():", my_list, "| Popped element:", popped_element)

# sort(): Sorts the list in ascending order.
unsorted_list = [3, 1, 4, 2]
unsorted_list.sort()
print("Sorted list:", unsorted_list)

# reverse(): Reverses the list in place.
unsorted_list.reverse()
print("Reversed list:", unsorted_list)

# clear(): Removes all elements from the list.
temp_list = [1, 2, 3]
temp_list.clear()
print("After clear():", temp_list)

print()

# ------------------------------------------------------------------------------
# SECTION 4: Iterating Over Lists
# ------------------------------------------------------------------------------
print("=== SECTION 4: ITERATING OVER LISTS ===")

colors = ["red", "green", "blue"]

# Using a for loop
print("Iterating using for loop:")
for color in colors:
    print("Color:", color)

# Using list indices
print("Iterating using indices:")
for i in range(len(colors)):
    print(f"colors[{i}] = {colors[i]}")

# Using list comprehension to create a new list (e.g., uppercase versions)
uppercase_colors = [color.upper() for color in colors]
print("Uppercase colors:", uppercase_colors)

print()

# ------------------------------------------------------------------------------
# SECTION 5: Nested Lists (Lists of Lists)
# ------------------------------------------------------------------------------
print("=== SECTION 5: NESTED LISTS ===")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix:
    print(row)

# Accessing an element in a nested list:
print("Element at row 2, column 3 (matrix[1][2]):", matrix[1][2])

print()

# ------------------------------------------------------------------------------
# SECTION 6: List Comprehensions
# ------------------------------------------------------------------------------
print("=== SECTION 6: LIST COMPREHENSIONS ===")

# Creating a list of squares for numbers 0-9
squares = [x**2 for x in range(10)]
print("List of squares (0-9):", squares)

# List comprehension with a condition: even squares only
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares (0-9):", even_squares)

# Nested list comprehension: Flatten a matrix (2D list) into 1D list
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# More complex example: Create a list of tuples (number, square)
number_square_pairs = [(x, x**2) for x in range(5)]
print("Number and square pairs:", number_square_pairs)

# ------------------------------------------------------------------------------
# END OF SCRIPT
# ------------------------------------------------------------------------------
print("End of 03_lists.py")
