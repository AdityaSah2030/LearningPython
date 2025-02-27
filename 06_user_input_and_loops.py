"""
This script demonstrates:
1. Getting user input using the input() function.
2. Converting input strings to appropriate types.
3. Using a while loop for repeated user input and accumulation.
4. Using for loops to iterate over lists and ranges.
5. Using loop control statements: break, continue, and pass.
6. Nested loops: creating a multiplication table.

How to run:
    python 06_user_input_and_loops.py
Note: Some sections require user interaction. Please follow the prompts.
"""

# ------------------------------------------------------------------------------
# SECTION 1: Basic User Input
# ------------------------------------------------------------------------------
print("=== SECTION 1: BASIC USER INPUT ===")
user_name = input("Please enter your name: ")
print(f"Hi {user_name}, let's explore loops in Python!\n")

# ------------------------------------------------------------------------------
# SECTION 2: While Loop Example - Summing Numbers
# ------------------------------------------------------------------------------
print("=== SECTION 2: WHILE LOOP EXAMPLE ===")
print("Enter numbers to sum them up. Type 'done' to finish.")

total = 0  # Initialize accumulator
while True:
    user_input = input("Enter a number (or 'done'): ")
    if user_input.lower() == 'done':
        # Exit the loop when user types 'done'
        break
    try:
        number = float(user_input)  # Convert input to float for numerical addition
        total += number
    except ValueError:
        # If conversion fails, notify the user and skip to the next iteration
        print("Invalid input. Please enter a valid number.")
        continue  # Skip to the next iteration

print(f"The total sum is: {total}\n")

# ------------------------------------------------------------------------------
# SECTION 3: For Loop Examples
# ------------------------------------------------------------------------------
print("=== SECTION 3: FOR LOOP EXAMPLES ===")

# Example 1: Iterating over a list of items
colors = ["red", "green", "blue", "yellow"]
print("Listing colors from a list:")
for color in colors:
    print(color)

print()  # Blank line for readability

# Example 2: Iterating using range()
print("Printing numbers from 0 to 4 using range():")
for i in range(5):
    print(i)

print()  # Blank line

# ------------------------------------------------------------------------------
# SECTION 4: Loop Control Statements (break, continue, pass)
# ------------------------------------------------------------------------------
print("=== SECTION 4: LOOP CONTROL STATEMENTS ===")

# Using 'continue' to skip even numbers: print only odd numbers from 0 to 9
print("Printing odd numbers (using 'continue'):")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(i)

print()  # Blank line

# Using 'pass' as a placeholder (no operation is performed)
print("Demonstrating 'pass' (placeholder in a loop):")
for i in range(3):
    pass  # No action taken, useful for future code structure
print("Loop with 'pass' completed.\n")

# Using 'break' to exit a loop early
print("Using 'break' to exit the loop when a condition is met:")
for i in range(10):
    if i == 5:
        print("Reached 5, breaking out of the loop.")
        break
    print(i)

print()  # Blank line

# ------------------------------------------------------------------------------
# SECTION 5: Nested Loops - Multiplication Table
# ------------------------------------------------------------------------------
print("=== SECTION 5: NESTED LOOPS - MULTIPLICATION TABLE ===")
print("Multiplication table for numbers 1 through 5:")

# Nested loops: outer loop for rows, inner loop for columns
for i in range(1, 6):  # Numbers 1 through 5
    for j in range(1, 6):
        # Print the product formatted in a field of width 2, followed by a space
        print(f"{i * j:2d}", end=" ")
    print()  # Newline after each row

# ------------------------------------------------------------------------------
# END OF SCRIPT
# ------------------------------------------------------------------------------
print("\nEnd of 06_user_input_and_loops.py")
