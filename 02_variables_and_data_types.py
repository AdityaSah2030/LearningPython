"""
This script demonstrates:
1) Variables and assignment
2) Core data types: int, float, bool, str, complex
3) Type conversion (casting)
4) Basic operators (arithmetic, comparison, logical)
5) The math library
6) The random library
7) The decimal library
8) range() function
9) Number systems (binary, octal, hex)
10) Strings: indexing, slicing, methods (split, join, format, etc.)

How to run:
    python 02_variables_and_data_types.py
"""

# ------------------------------------------------------------------------------
# SECTION 1: Variables and Basic Data Types
# ------------------------------------------------------------------------------
print("=== SECTION 1: VARIABLES & BASIC DATA TYPES ===")

# Python variables are created by assigning a value to a name:
my_int = 10
my_float = 3.14
my_bool = True
my_str = "Hello, Python!"
my_complex = 2 + 3j  # Complex number (2 + 3i)

# Python is dynamically typed, so we can reassign different types to the same variable:
my_var = 100
print("my_var (int):", my_var)
my_var = "Now I'm a string!"
print("my_var (str):", my_var)

print("my_int:", my_int, "->", type(my_int))
print("my_float:", my_float, "->", type(my_float))
print("my_bool:", my_bool, "->", type(my_bool))
print("my_str:", my_str, "->", type(my_str))
print("my_complex:", my_complex, "->", type(my_complex))
print()

# ------------------------------------------------------------------------------
# SECTION 2: Type Conversion (Casting)
# ------------------------------------------------------------------------------
print("=== SECTION 2: TYPE CONVERSION (CASTING) ===")

num_str = "50"
num_int = int(num_str)   # Convert string to int
num_float = float(num_str)  # Convert string to float
bool_val = bool(num_str) # Any non-empty string is True when converted to bool

print(f"num_str = '{num_str}' -> int: {num_int}, float: {num_float}, bool: {bool_val}")

# Converting float to int (truncates decimal part)
pi = 3.14159
pi_int = int(pi)
print("float pi:", pi, "-> int:", pi_int)

# Converting int to string
age = 25
age_str = str(age)
print("int age:", age, "-> str:", age_str)

print()

# ------------------------------------------------------------------------------
# SECTION 3: Basic Operators
# ------------------------------------------------------------------------------
print("=== SECTION 3: BASIC OPERATORS ===")

a = 10
b = 3

# Arithmetic Operators
print(f"{a} + {b} =", a + b)
print(f"{a} - {b} =", a - b)
print(f"{a} * {b} =", a * b)
print(f"{a} / {b} =", a / b)       # Floating-point division
print(f"{a} // {b} =", a // b)     # Integer (floor) division
print(f"{a} % {b} =", a % b)       # Modulus
print(f"{a} ** {b} =", a ** b)     # Exponentiation

# Comparison Operators
print(f"{a} > {b}:", a > b)
print(f"{a} == {b}:", a == b)
print(f"{a} != {b}:", a != b)

# Logical Operators
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print()

# ------------------------------------------------------------------------------
# SECTION 4: The math Library
# ------------------------------------------------------------------------------
print("=== SECTION 4: THE math LIBRARY ===")

import math

print("math.pi:", math.pi)
print("math.e:", math.e)
print("math.sqrt(16):", math.sqrt(16))
print("math.factorial(5):", math.factorial(5))
print("math.sin(math.pi/2):", math.sin(math.pi / 2))

print()

# ------------------------------------------------------------------------------
# SECTION 5: The random Library
# ------------------------------------------------------------------------------
print("=== SECTION 5: THE random LIBRARY ===")

import random

# random.random() -> returns a float in [0.0, 1.0)
rand_float = random.random()
print("random.random():", rand_float)

# random.randint(a, b) -> returns an int between a and b (inclusive)
rand_int = random.randint(1, 10)
print("random.randint(1, 10):", rand_int)

# random.choice(sequence) -> returns a random element from the sequence
fruits = ["apple", "banana", "cherry", "date"]
chosen_fruit = random.choice(fruits)
print("random.choice(fruits):", chosen_fruit)

print()

# ------------------------------------------------------------------------------
# SECTION 6: The decimal Library
# ------------------------------------------------------------------------------
print("=== SECTION 6: THE decimal LIBRARY ===")

from decimal import Decimal, getcontext

# Set precision for decimal operations
getcontext().prec = 5  # set precision to 5 digits
dec_a = Decimal("1.12345")
dec_b = Decimal("2.34567")
dec_sum = dec_a + dec_b
print("Decimal sum:", dec_sum)

# Observe how precision affects the result
getcontext().prec = 3
dec_c = Decimal("1.12345")
dec_d = Decimal("2.34567")
dec_sum2 = dec_c + dec_d
print("Decimal sum with precision=3:", dec_sum2)

print()

# ------------------------------------------------------------------------------
# SECTION 7: The range() Function
# ------------------------------------------------------------------------------
print("=== SECTION 7: THE range() FUNCTION ===")

# range(stop) -> from 0 to stop-1
for i in range(3):
    print("i in range(3):", i)

# range(start, stop, step)
for i in range(2, 10, 2):
    print("i in range(2, 10, 2):", i)

print()

# ------------------------------------------------------------------------------
# SECTION 8: Number Systems (Binary, Octal, Hex)
# ------------------------------------------------------------------------------
print("=== SECTION 8: NUMBER SYSTEMS (BINARY, OCTAL, HEX) ===")

num = 25
bin_rep = bin(num)   # binary representation (base 2)
oct_rep = oct(num)   # octal representation (base 8)
hex_rep = hex(num)   # hexadecimal representation (base 16)

print(f"{num} in binary:", bin_rep)
print(f"{num} in octal:", oct_rep)
print(f"{num} in hex:", hex_rep)

# Convert from string representations to int
print("int('11001', 2) ->", int('11001', 2))  # '11001' is binary for 25
print("int('31', 8) ->", int('31', 8))        # '31' is octal for 25
print("int('19', 16) ->", int('19', 16))      # '19' is hex for 25
print()

# ------------------------------------------------------------------------------
# SECTION 9: Strings - Indexing, Slicing, Methods
# ------------------------------------------------------------------------------
print("=== SECTION 9: STRINGS (INDEXING, SLICING, METHODS) ===")

my_string = "Hello, Python!"
print("Original String:", my_string)

# Indexing
print("my_string[0]:", my_string[0])     # First character
print("my_string[-1]:", my_string[-1])   # Last character

# Slicing
print("my_string[0:5]:", my_string[0:5])       # Characters 0 to 4
print("my_string[:5]:", my_string[:5])         # Start to index 4
print("my_string[7:]:", my_string[7:])         # Index 7 to end
print("my_string[::2]:", my_string[::2])       # Every 2nd character

# Common String Methods
upper_str = my_string.upper()
lower_str = my_string.lower()
split_str = my_string.split(",")   # Split on comma
joined_str = " ".join(["Join", "these", "words"])
formatted_str = f"{my_string} - length is {len(my_string)}"

print("Uppercase:", upper_str)
print("Lowercase:", lower_str)
print("Split on comma:", split_str)
print("Joined string:", joined_str)
print("Formatted string:", formatted_str)

# repr() usage
raw_repr = repr(my_string)
print("repr(my_string):", raw_repr)

# format() usage
formatted_num = "Pi approx: {:.2f}".format(3.14159)
print(formatted_num)

print()

# ------------------------------------------------------------------------------
# END OF SCRIPT
# ------------------------------------------------------------------------------
print("End of 02_variables_and_data_types.py")
