"""
This script demonstrates:
1. Basic if statements
2. if-elif-else structures
3. Nested if statements
4. Logical operators (and, or, not) in conditions
5. Ternary (conditional) operators for concise expressions

How to run:
    python 04_if_statements.py
"""

# ------------------------------------------------------------------------------
# SECTION 1: Basic if Statements
# ------------------------------------------------------------------------------
print("=== SECTION 1: BASIC if STATEMENTS ===")

age = 20
if age >= 18:
    print("You are an adult.")
print("This line always executes regardless of the if condition.")

# ------------------------------------------------------------------------------
# SECTION 2: if-elif-else Structures
# ------------------------------------------------------------------------------
print("\n=== SECTION 2: if-elif-else STRUCTURE ===")

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Score:", score, "| Grade:", grade)

# ------------------------------------------------------------------------------
# SECTION 3: Nested if Statements
# ------------------------------------------------------------------------------
print("\n=== SECTION 3: NESTED if STATEMENTS ===")

# Example: Checking user eligibility for a senior discount
age = 65
has_discount_card = True

if age >= 60:
    print("Eligible for senior benefits.")
    if has_discount_card:
        print("Discount card validated. You get an extra discount!")
    else:
        print("No discount card provided. Consider applying for one.")
else:
    print("Not eligible for senior benefits.")

# ------------------------------------------------------------------------------
# SECTION 4: Using Logical Operators
# ------------------------------------------------------------------------------
print("\n=== SECTION 4: LOGICAL OPERATORS IN CONDITIONS ===")

temperature = 72
humidity = 45

# Checking multiple conditions with 'and'
if temperature > 70 and humidity < 50:
    print("It's a warm and dry day.")

# Using 'or'
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# Using 'not'
is_raining = False
if not is_raining:
    print("It's not raining; enjoy your day!")

# ------------------------------------------------------------------------------
# SECTION 5: Ternary (Conditional) Operator
# ------------------------------------------------------------------------------
print("\n=== SECTION 5: TERNARY OPERATOR ===")

# Traditional if-else to assign a message
if age >= 18:
    status = "adult"
else:
    status = "minor"
print("Traditional:", status)

# Ternary operator for concise assignment
status = "adult" if age >= 18 else "minor"
print("Ternary:", status)

# Another example: Choosing a message based on a condition
temperature = 60
message = "It's warm." if temperature > 65 else "It's cool."
print("Temperature message:", message)

# ------------------------------------------------------------------------------
# END OF SCRIPT
# ------------------------------------------------------------------------------
print("\nEnd of 04_if_statements.py")
