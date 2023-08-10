"""
Generator: Generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
A generator has special type of function called yield. Yield is a keyword that is used like return,
except the function will return a generator.

Basically yield stop the function and return the value and when the function is called again it will continue
from where it was left off.

Syntax:
        def generator_function(num):
            for i in range(num):
                yield i


"""


def generator_function(num):
    for i in range(num):
        yield i


for item in generator_function(1000):
    print(item)

g = generator_function(1000)
print(next(g))
print(next(g))

# Here we are not creating a list of 1000 numbers. We are just creating a generator function which will return
# 1000 numbers one by one. So it will not take much time to create a list of 1000 numbers.

# Compare this snippet from generators\generator 02 (Creating our own generator).py:
"""
# range(100)
# list(range(100))


def make_list(num):
    result = []

    for i in range(num):
        result.append(i * 2)
    return result

my_list = make_list(100)
print(my_list)
"""
