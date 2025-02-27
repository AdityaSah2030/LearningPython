"""
This script demonstrates:
1. Defining and calling functions.
2. Parameters, return values, and scope.
3. Default parameters.
4. Variable-length arguments (*args and **kwargs).
5. Lambda (anonymous) functions.
6. Recursion with a factorial example.
7. Functions as first-class citizens (passing functions as arguments).
8. Function annotations (type hints).

How to run:
    python 07_functions.py
"""

# ------------------------------------------------------------------------------
# SECTION 1: Basic Function Definition and Call
# ------------------------------------------------------------------------------
print("=== SECTION 1: BASIC FUNCTION DEFINITION ===")

def greet():
    """A simple function that prints a greeting."""
    print("Hello! Welcome to Python functions.")

# Calling the function
greet()

print()  # Blank line for readability

# ------------------------------------------------------------------------------
# SECTION 2: Functions with Parameters and Return Values
# ------------------------------------------------------------------------------
print("=== SECTION 2: PARAMETERS AND RETURN VALUES ===")

def add(a, b):
    """
    Returns the sum of two numbers.
    
    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The sum of a and b.
    """
    return a + b

result = add(5, 7)
print("5 + 7 =", result)

# ------------------------------------------------------------------------------
# SECTION 3: Default Parameters
# ------------------------------------------------------------------------------
print("\n=== SECTION 3: DEFAULT PARAMETERS ===")

def introduce(name, age=25):
    """
    Introduces a person with a name and age. Default age is 25 if not provided.
    
    Parameters:
        name (str): The person's name.
        age (int, optional): The person's age.
    """
    print(f"My name is {name} and I am {age} years old.")

# Calling with both parameters
introduce("Alice", 30)
# Calling with only the mandatory parameter; uses default age
introduce("Bob")

# ------------------------------------------------------------------------------
# SECTION 4: Variable-Length Arguments (*args and **kwargs)
# ------------------------------------------------------------------------------
print("\n=== SECTION 4: VARIABLE-LENGTH ARGUMENTS ===")

def show_args(*args):
    """
    Accepts any number of positional arguments and prints them.
    """
    print("Positional arguments:", args)

def show_kwargs(**kwargs):
    """
    Accepts any number of keyword arguments and prints them.
    """
    print("Keyword arguments:", kwargs)

show_args(1, 2, 3, "hello")
show_kwargs(a=1, b=2, c="world")

def mix_arguments(x, *args, **kwargs):
    """
    Demonstrates a function that accepts a mandatory parameter, 
    variable-length positional arguments, and variable-length keyword arguments.
    """
    print("Mandatory argument:", x)
    print("Additional positional arguments:", args)
    print("Additional keyword arguments:", kwargs)

mix_arguments("Required", 10, 20, key1="value1", key2="value2")

# ------------------------------------------------------------------------------
# SECTION 5: Lambda (Anonymous) Functions
# ------------------------------------------------------------------------------
print("\n=== SECTION 5: LAMBDA FUNCTIONS ===")

# Lambda function to square a number
square = lambda x: x * x
print("Square of 5 using lambda:", square(5))

# Lambda used with a higher-order function (map)
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers (using map and lambda):", squared_numbers)

# ------------------------------------------------------------------------------
# SECTION 6: Recursion - Factorial Example
# ------------------------------------------------------------------------------
print("\n=== SECTION 6: RECURSION (FACTORIAL) ===")

def factorial(n):
    """
    Recursively computes the factorial of n.
    
    Parameters:
        n (int): A non-negative integer.
    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"Factorial of {num} is:", factorial(num))

# ------------------------------------------------------------------------------
# SECTION 7: Functions as First-Class Citizens
# ------------------------------------------------------------------------------
print("\n=== SECTION 7: FUNCTIONS AS FIRST-CLASS CITIZENS ===")

def shout(text):
    """Converts text to uppercase and adds an exclamation."""
    return text.upper() + "!"

def whisper(text):
    """Converts text to lowercase and adds ellipsis."""
    return text.lower() + "..."

def speak(func, message):
    """
    Accepts a function (func) as a parameter and applies it to message.
    
    Parameters:
        func (callable): A function that takes a string and returns a string.
        message (str): The message to be processed.
    """
    print(func(message))

# Passing functions as arguments
speak(shout, "Hello there")
speak(whisper, "Hello there")

# ------------------------------------------------------------------------------
# SECTION 8: Function Annotations (Type Hints)
# ------------------------------------------------------------------------------
print("\n=== SECTION 8: FUNCTION ANNOTATIONS (TYPE HINTS) ===")

def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers.
    
    Parameters:
        a (int): The first integer.
        b (int): The second integer.
    Returns:
        int: The product of a and b.
    """
    return a * b

print("Multiplying 4 and 5 gives:", multiply(4, 5))

# ------------------------------------------------------------------------------
# END OF SCRIPT
# ------------------------------------------------------------------------------
print("\nEnd of 07_functions.py")
