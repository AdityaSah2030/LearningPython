from functools import wraps   # helps keep the original function's metadata

# A simple decorator function
def my_decorator(func):
    @wraps(func)              # preserves original function name, docstring, etc.
    def wrapper():
        print("Before function runs")
        func()                # call the actual function
        print("After function runs")
    return wrapper            # return the wrapped function

# Applying the decorator using @ syntax
@my_decorator
def greet():
    print("Hello from decorators class from chaicode")

greet()  
# When greet() is called: It actually runs wrapper() (because greet has been decorated)

print(greet.__name__)  
# Normally, without @wraps, this would print "wrapper"
# But because we used @wraps(func), it correctly prints "greet"
# This shows that @wraps preserved the original function metadata