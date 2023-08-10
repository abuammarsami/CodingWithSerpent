#decorator

"""
SO what is happening here. We are creating a function called my_decorator. This function takes another function as a
parameter. And then we are creating a function called wrap_func. This function will print some stars and then call the
function that was passed to it. And then we are returning the wrap_func function. So what we are doing here is we are
wrapping the function that was passed to my_decorator function. So we are creating a wrapper function around the function
that was passed to my_decorator function. And then we are returning the wrapper function. So we are returning the
wrap_func function.

The syntax of decorator is:
                A decorator is a function that takes another function as an argument and adds some functionality and
                then returns another function without altering the source code of the original function passed in.

                Or

                A decorator is a function that accepting a function having a wrapper function calling the function and
                returning the wrapper function.
"""

def my_decorator(func):
    def wrap_func():
        print('***********')
        func()
        print('***********')
    return wrap_func

@my_decorator # this is the same as saying hello = my_decorator(hello).
def hello():
    print('hellooooooo')

hello()

#my_decorator(hello)()
