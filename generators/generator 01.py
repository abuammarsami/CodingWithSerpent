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
Now imagine you have to create a list of 1000000 numbers. Then it will take a lot of time to create that list.
So in python we have a generator. A generator is a function that returns an object (iterator)
which we can iterate over (one value at a time). A generator has special type of function called yield. 
Yield is a keyword that is used like return, except the function will return a generator. 
 




"""