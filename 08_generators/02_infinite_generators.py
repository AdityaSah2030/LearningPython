# A generator function that gives infinite "refills"
def infinite_chai():
    count = 1
    while True:
        # yield pauses here and returns the value
        yield f"Refill #{count}"
        count += 1   # increase the count for the next refill

# Create two independent generator objects
refill = infinite_chai()
user2 = infinite_chai()

# First user takes 5 refills
print("User 1 Refills:")
for _ in range(5):
    print(next(refill))

# Second user takes 6 refills
print("\nUser 2 Refills:")
for _ in range(6):
    print(next(user2))

"""
Note:
- Each generator (refill, user2) is independent.
- When we call next() on one generator, it doesn’t affect the other.
- That's why both start at "Refill #1".
"""