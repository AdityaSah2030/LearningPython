"""
This script demonstrates:
1. Basic try-except blocks to catch errors.
2. Using else and finally clauses in exception handling.
3. Raising exceptions explicitly with raise.
4. Creating and handling custom exceptions.
5. Handling multiple exception types.

How to run:
    python 10_exception_handling.py
"""

# ------------------------------------------------------------------------------
# SECTION 1: Basic try-except Blocks
# ------------------------------------------------------------------------------
print("=== SECTION 1: BASIC try-except BLOCKS ===")

# Example: Handling division by zero
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Example: Catching a ValueError during type conversion
try:
    user_input = "abc"  # Non-numeric string
    number = int(user_input)
    print("Converted number:", number)
except ValueError:
    print("Error: Invalid input! Please enter a numeric value.")

print()

# ------------------------------------------------------------------------------
# SECTION 2: Using else and finally
# ------------------------------------------------------------------------------
print("=== SECTION 2: else and finally ===")

try:
    number = int("123")
except ValueError:
    print("Conversion failed!")
else:
    # This block runs if no exception was raised
    print("Conversion successful. Number is:", number)
finally:
    # This block always executes, regardless of exceptions
    print("Execution of try-except block complete.")

print()

# ------------------------------------------------------------------------------
# SECTION 3: Raising Exceptions with raise
# ------------------------------------------------------------------------------
print("=== SECTION 3: RAISING EXCEPTIONS ===")

def check_positive(number):
    """
    Raises a ValueError if the number is not positive.
    """
    if number <= 0:
        raise ValueError("Number must be positive.")
    return number

try:
    value = check_positive(-5)
    print("Value:", value)
except ValueError as e:
    print("Caught an exception:", e)

print()

# ------------------------------------------------------------------------------
# SECTION 4: Custom Exceptions
# ------------------------------------------------------------------------------
print("=== SECTION 4: CUSTOM EXCEPTIONS ===")

# Define a custom exception by extending the Exception class
class InsufficientBalanceError(Exception):
    """Exception raised when a bank account has insufficient balance for a withdrawal."""
    def __init__(self, balance, amount, message="Insufficient balance for withdrawal."):
        self.balance = balance
        self.amount = amount
        self.message = message
        super().__init__(self.message)

# A sample BankAccount class that uses the custom exception
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

# Demonstrate custom exception handling
account = BankAccount("Eve", 100)
account.deposit(50)
try:
    account.withdraw(200)
except InsufficientBalanceError as e:
    print(f"Custom Exception Caught: {e.message} (Balance: {e.balance}, Attempted Withdrawal: {e.amount})")

print()

# ------------------------------------------------------------------------------
# SECTION 5: Handling Multiple Exceptions
# ------------------------------------------------------------------------------
print("=== SECTION 5: HANDLING MULTIPLE EXCEPTIONS ===")

try:
    # This block may raise either ValueError or ZeroDivisionError
    x = int("not_a_number")  # Will raise ValueError
    y = 10 / 0              # Would raise ZeroDivisionError if executed
except ValueError:
    print("Caught a ValueError: Invalid conversion!")
except ZeroDivisionError:
    print("Caught a ZeroDivisionError: Division by zero!")
except Exception as e:
    # A generic catch-all for any other exceptions
    print("Caught an unexpected exception:", e)
else:
    print("No exceptions were raised!")
finally:
    print("Finished handling multiple exceptions.")

# ------------------------------------------------------------------------------
# END OF SCRIPT
# ------------------------------------------------------------------------------
print("\nEnd of 10_exception_handling.py")
