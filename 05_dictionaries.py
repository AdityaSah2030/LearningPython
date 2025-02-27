"""
This script demonstrates:
1. Creating dictionaries and accessing key-value pairs.
2. Adding, updating, and removing items.
3. Common dictionary methods (keys, values, items, get, update, pop, etc.).
4. Iterating over dictionaries.
5. Nested dictionaries.
6. Dictionary comprehensions.

How to run:
    python 05_dictionaries.py
"""

# ------------------------------------------------------------------------------
# SECTION 1: Creating and Accessing Dictionaries
# ------------------------------------------------------------------------------
print("=== SECTION 1: CREATING AND ACCESSING DICTIONARIES ===")

# Creating a dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Person dictionary:", person)

# Accessing values using keys
print("Name:", person["name"])
print("Age:", person.get("age"))  # Using get() which is safe if key is absent

# ------------------------------------------------------------------------------
# SECTION 2: Adding, Updating, and Removing Elements
# ------------------------------------------------------------------------------
print("\n=== SECTION 2: ADDING, UPDATING, AND REMOVING ELEMENTS ===")

# Adding a new key-value pair
person["occupation"] = "Engineer"
print("After adding occupation:", person)

# Updating an existing key
person["age"] = 31
print("After updating age:", person)

# Removing an element using del keyword
del person["city"]
print("After deleting city:", person)

# Removing an element using pop() which also returns the value
removed_value = person.pop("occupation")
print("After popping occupation:", person, "| Removed value:", removed_value)

# ------------------------------------------------------------------------------
# SECTION 3: Dictionary Methods
# ------------------------------------------------------------------------------
print("\n=== SECTION 3: COMMON DICTIONARY METHODS ===")

sample_dict = {"a": 1, "b": 2, "c": 3}
print("Sample Dictionary:", sample_dict)

# keys(): Returns a view of all keys
print("Keys:", list(sample_dict.keys()))

# values(): Returns a view of all values
print("Values:", list(sample_dict.values()))

# items(): Returns a view of key-value pairs
print("Items:", list(sample_dict.items()))

# update(): Merges another dictionary into sample_dict
sample_dict.update({"d": 4, "e": 5})
print("After update:", sample_dict)

# clear(): Removes all items from the dictionary
temp_dict = {"x": 10, "y": 20}
temp_dict.clear()
print("After clear:", temp_dict)

# ------------------------------------------------------------------------------
# SECTION 4: Iterating Over Dictionaries
# ------------------------------------------------------------------------------
print("\n=== SECTION 4: ITERATING OVER DICTIONARIES ===")

student_grades = {
    "John": "A",
    "Emma": "B",
    "Peter": "C"
}

# Iterating over keys
print("Iterating over keys:")
for student in student_grades:
    print(student, "->", student_grades[student])

# Iterating using items() to get key-value pairs directly
print("\nIterating using items():")
for student, grade in student_grades.items():
    print(f"{student} scored {grade}")

# ------------------------------------------------------------------------------
# SECTION 5: Nested Dictionaries
# ------------------------------------------------------------------------------
print("\n=== SECTION 5: NESTED DICTIONARIES ===")

# Example of a nested dictionary: a dictionary of dictionaries
students = {
    "Alice": {"age": 25, "major": "Physics"},
    "Bob": {"age": 22, "major": "Computer Science"},
    "Charlie": {"age": 23, "major": "Mathematics"}
}

# Access nested values
print("Alice's major:", students["Alice"]["major"])

# Iterating over nested dictionaries
for student, details in students.items():
    print(f"{student}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

# ------------------------------------------------------------------------------
# SECTION 6: Dictionary Comprehensions
# ------------------------------------------------------------------------------
print("\n=== SECTION 6: DICTIONARY COMPREHENSIONS ===")

# Creating a dictionary of squares for numbers 0-4
squares = {x: x**2 for x in range(5)}
print("Squares dictionary:", squares)

# Conditional dictionary comprehension:
# Create a dictionary of even numbers and their squares for numbers 0-9
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even squares dictionary:", even_squares)

# ------------------------------------------------------------------------------
# END OF SCRIPT
# ------------------------------------------------------------------------------
print("\nEnd of 05_dictionaries.py")
