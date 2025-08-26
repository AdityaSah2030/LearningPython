# generator function
def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

for cup in stall:
    print(cup)

# Cup 1: Masala Chai
# Cup 2: Ginger Chai
# Cup 3: Elaichi Chai


chai = serve_chai()

print(next(chai))   # Cup 1: Masala Chai
print(next(chai))   # Cup 2: Ginger Chai
print(next(chai))   # Cup 3: Elaichi Chai
# print(next(chai)) # Gives error