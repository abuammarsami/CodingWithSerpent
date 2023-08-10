def hello():
    print('hellooooooo')


greet = hello

del hello  # this will delete the hello function from memory. So if you call the hello function, it will give you an
# error. But greet function will still work. Because greet is still pointing to the hello function. So it will still.

""" 
So function in python act just like variable do they are first class citizen. we can assign them to a variable, we can 
pass them as a parameter to another function, we can return them from a function. 

def greet():
    print('still here')   

So why we are talking about this. Because we can use this to create a decorator. Underneath the hood, a decorator is
just a function that takes another function as an argument and returns another function. 
"""

greet()

# Higer Order Function HOC: A function that either accepts a function as a parameter or returns a function or both.

def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func