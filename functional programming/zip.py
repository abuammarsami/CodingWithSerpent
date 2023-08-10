# map, filter, reduce, zip, map, lambda
# map - takes a function and an iterable, returns a new iterable with the function applied to each item
print('\nmap')


# map(function, iterable, ...) Return an iterator that applies function to every item of iterable, yielding the
# results. If additional iterable arguments are passed, function must take that many arguments and is applied to the
# items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is
# exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().
# If function is None, the identity function is assumed; if there are multiple arguments, map() returns a list
# consisting of tuples containing the corresponding items from all iterables (a kind of transpose operation). The
# iterable arguments may be a sequence or any iterable object; the result is always a list.

def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, [1, 2, 3])))

# filter - takes a function and an iterable, returns a new iterable with the items that return true when passed into
# the function
print('\nfilter')


# filter(function or None, iterable) Construct an iterator from those elements of iterable for which function returns
# true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None,
# the identity function is assumed, that is, all elements of iterable that are false are removed. Note that filter(
# function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) if
# function is not None and (item for item in iterable if item) if function is None.

def only_odd(item):
    return item % 2 != 0


print(list(map(only_odd, [1, 2, 3])))
print(list(filter(only_odd, [1, 2,
                             3])))  # so basically it filter out the values from a list based on true and false
# according to the condition.

# zip - takes any number of iterables, returns an iterator of tuples, where the i-th tuple contains the i-th element
# from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted.
# With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.
print('\nzip')
# zip(*iterables) Make an iterator that aggregates elements from each of the iterables. Returns an iterator of
# tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The
# iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an
# iterator of 1-tuples. With no arguments, it returns an empty iterator. Equivalent to: def zip(*iterables): # zip(
# 'ABCD', 'xy') --> Ax By

print(list(zip([1, 2, 3], [4, 5, 6])))

# reduce - takes a function and an iterable and returns a single value calculated by calling the function with the
# accumulated result and the next item in the sequence
print('\nreduce')
# reduce(function, sequence[, initial]) -> value Apply a function of two arguments cumulatively to the items of a
# sequence, from left to right, so as to reduce the sequence to a single value. For example, reduce(lambda x, y: x+y,
# [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). If initial is present, it is placed before the items of the sequence
# in the calculation, and serves as a default when the sequence is empty. If reduce() is given only one argument,
# it returns the single item of the sequence. If the sequence is empty, with no initial value, it raises a TypeError.

from functools import reduce


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, [1, 2, 3], 0))

# lambda - creates an anonymous function
print('\nlambda')

"""
lambda arguments : expression lembda is a small anonymous function. A lambda function can take any number of 
arguments, but can only have one expression. Very similar to a def function, but has no name. It can be used when a
function is required for a short period of time. 

syntax:
    lambda arguments/ parameter : expression 
"""

print(list(map(lambda item: item * 2, [1, 2, 3])))
print(list(filter(lambda item: item % 2 != 0, [1, 2, 3])))
print(reduce(lambda acc, item: acc + item, [1, 2, 3], 0))
