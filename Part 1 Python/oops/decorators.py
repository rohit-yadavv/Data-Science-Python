'''

In Python, decorators are a way to modify or enhance functions or methods without changing their actual code. 
They allow you to add functionality in a clean, readable, and reusable manner. 
Decorators are often used for logging, enforcing access control, instrumentation, or modifying behavior in functions or methods.

'''

def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()  # Call the original function
        print("Something after the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# my_decorator: A decorator function that takes say_hello as an argument.

# wrapper: An inner function that adds additional behavior (printing before and after calling the say_hello function).

# @my_decorator: This applies the my_decorator to the say_hello function. It’s equivalent to writing say_hello = my_decorator(say_hello).


def greet(fx):
  def mfx(*args, **kwargs):
    print("good morning")
    fx(*args, **kwargs)
    print("thanks for using fxn")
  return mfx

def add(a, b):
  print(a+b)

# greet(add)(1, 2)

@greet 
def add(a, b):
  print(a+b)

add(1, 2)