def idle_chaiwala():
    pass

print(idle_chaiwala())

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"
    print("chai")

print(chai_status(0))
print(chai_status(5))

def chai_report():
    return 100, 20, 10 # sold, remaining

sold, remaining, not_paid = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)