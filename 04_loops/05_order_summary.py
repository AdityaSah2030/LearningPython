names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")

# zip(names, bills) pairs elements from both lists together:
# ("Hitesh", 50), ("Meera", 70), ("Sam", 100), ("Ali", 55)
# This allows iterating over them in parallel.