class Chai:
    # Class attributes (shared by all instances if not overridden)
    temperature = "Hot"
    strength = "Strong"

# Create an object (instance) of class Chai
cutting = Chai()

# Accessing class attribute via instance
print(cutting.temperature)   # Output: Hot

# Override the class attribute on THIS instance only
cutting.temperature = "Mild"  # now instance has its own 'temperature'
cutting.cup = "Small"         # new instance attribute (not in class)
print("After changing ", cutting.temperature)  # Output: Mild
print("Cup size is  ", cutting.cup)            # Output: Small

# Looking directly at the class attribute
print("Direct look into the class ", Chai.temperature)  # Output: Hot


# Delete the instance attributes
del cutting.temperature   # removes the instance-level 'temperature'
del cutting.cup           # removes the instance-level 'cup'

print(cutting.temperature)
# Since instance attribute 'temperature' was deleted,
# Python falls back to the class attribute → Output: Hot

print(cutting.cup)
# 'cup' was never a class attribute, only an instance attribute.
# After deletion, Python looks into the class but doesn't find 'cup',
# So it raises: AttributeError: 'Chai' object has no attribute 'cup'