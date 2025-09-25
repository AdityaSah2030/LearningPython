class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0:
        raise OutOfIngredientsError("Missing Milk")
    if sugar == 0:
        raise OutOfIngredientsError("Missing Sugar")
    print("Chai is ready...")

make_chai(0, 1)