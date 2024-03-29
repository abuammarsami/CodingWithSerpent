# Decorators in Python

Decorators in Python are a powerful tool that allow us to modify the behavior of functions or methods. They are defined using a special syntax that involves nested functions.

In Python, a decorator is a function that takes another function as its argument, and extends or modifies the behavior of this input function without explicitly modifying it. This is achieved by defining a wrapper function inside the decorator that wraps the input function, providing additional functionality before or after the input function is called. The syntax for defining a decorator involves using the '@' symbol followed by the decorator function name before the function that needs to be decorated.

In this example, we define a decorator called 'performance' that measures the execution time of a function. The decorator is defined as a function that takes another function as an argument. Inside the decorator, we define a wrapper function that wraps the original function with additional behavior (in this case, measuring the execution time).

The '@' symbol is used to apply the decorator to a function. In this example, we apply the 'performance' decorator to the 'count' function using the '@performance' syntax.

Here is the code:

```python
from time import time

def performance(func):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} s')
    return wrapper_func

@performance
def count():
    for i in range(1, 1000000000):
        i * 5

count()