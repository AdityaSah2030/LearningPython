"""
This script demonstrates:
1. Checking your Python environment and version.
2. Different ways to write comments (single-line, multi-line, docstrings).
3. Basic print statements and how to run a Python file.
4. A brief example of mutable vs. immutable data in Python.

How to run:
    1. Open a terminal or command prompt.
    2. Navigate (cd) to the folder containing this file.
    3. Run "python 01_introduction_and_basic_setup.py" (without quotes).
"""

import sys

# ------------------------------------------------------------------------------
# SECTION 1: Checking Python Environment
# ------------------------------------------------------------------------------
print("=== PYTHON ENVIRONMENT CHECK ===")
print("Python Version:", sys.version)
print("Executable Path:", sys.executable)
print()  # Just a blank line for readability

# ------------------------------------------------------------------------------
# SECTION 2: Comments & Print Statements
# ------------------------------------------------------------------------------

# This is a single-line comment in Python.
# We use the hash (#) symbol for single-line comments.

"""
This is a multi-line string, often used for docstrings or 
large comments that span multiple lines. You can also use 
triple single-quotes (''') instead of triple double-quotes (""").
"""

print("=== PRINT STATEMENTS & COMMENTS ===")
print("Hello, world!")  # Basic greeting
print("You can print multiple items:", "like this", 123, 4.56)
print()  # Another blank line

# ------------------------------------------------------------------------------
# SECTION 3: Mutable vs. Immutable (Brief Introduction)
# ------------------------------------------------------------------------------
print("=== MUTABLE VS. IMMUTABLE ===")

# Immutable Data Types: int, float, bool, str, tuple, etc.
# Mutable Data Types: list, dict, set, etc.

# Example 1: Strings are IMMUTABLE
greeting = "Hello"
print("Original greeting:", greeting)
# If we 'change' the greeting, we actually create a new string object:
greeting = greeting + " World"
print("Modified greeting:", greeting)

# Example 2: Lists are MUTABLE
my_list = [1, 2, 3]
print("\nOriginal list:", my_list)
my_list.append(4)  # We are modifying the same list in-place
print("List after append:", my_list)

print()
# ------------------------------------------------------------------------------
# END OF SCRIPT
# ------------------------------------------------------------------------------
print("End of 01_introduction_and_basic_setup.py")
