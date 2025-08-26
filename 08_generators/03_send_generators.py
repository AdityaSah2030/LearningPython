def chai_customer():
    # This line runs only once when generator starts
    print("Welcome! \nWhat chai would you like?")
    
    # The generator pauses here and waits for a value from .send()
    order = yield

    # Infinite loop to keep accepting orders
    while True:
        # Print the current order
        print(f"Preparing: {order}")
        
        # Wait for the next order from .send()
        order = yield

# Create a generator object
stall = chai_customer()

# Start the generator. This runs code until the first 'yield'
# and pauses there, waiting for input.
next(stall)

# Now send values into the generator
stall.send("Masala Chai")   # resumes at 'order = yield', sets order = "Masala Chai"
stall.send("Lemon Chai")    # sets order = "Lemon Chai", prints it, then waits again


"""
How it works:
-------------
1. When we call next(stall):
    - Prints the welcome message
    - Pauses at 'order = yield', waiting for input

2. stall.send("Masala Chai"):
    - Assigns "Masala Chai" to variable 'order'
    - Prints "Preparing: Masala Chai"
    - Pauses again at the next 'order = yield'

3. stall.send("Lemon Chai"):
    - Assigns "Lemon Chai" to variable 'order'
    - Prints "Preparing: Lemon Chai"
    - Pauses again

Key Difference from 'next()':
- next() only moves to the next yield and *returns* values out.
- send(value) pushes a value *into* the generator at the paused yield.
"""