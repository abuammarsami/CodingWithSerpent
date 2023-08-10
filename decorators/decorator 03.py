#Decorator Pattern
def my_decorator (func):
    def wrapper_func(x, y):
        print('***************************')
        func(x, y)
        print('***************************')
    return wrapper_func

@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)

hello('Ammar',':)')

"""
Now if we want to pass more parameters to the hello function also keyword Argument, we can do that by using *args and **kwargs. So we can
pass any number of arguments to the hello function. And we can pass any number of keyword arguments to the hello 
function. 
"""

def my_decorator (func):
    def wrapper_func(*args, **kwargs):
        print('***************************')
        func(*args, **kwargs)
        print('***************************')
    return wrapper_func

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)

hello('Ammar')