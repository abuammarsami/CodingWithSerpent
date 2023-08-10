# Generators in Python

Generators in Python are a type of iterable, like lists or tuples. They do not allow indexing, but they can still be iterated through with for loops. They are created using functions and the 'yield' keyword.

The 'yield' keyword is used like return, except the function will return a generator. When a generator function is called, it returns a generator object without even beginning execution of the function. When 'next' is called for the first time, the function starts executing until it reaches the 'yield' keyword.

Here is an example of a generator function:

```python
def make_list(num):
    for i in range(num):
        yield i * 2
```

In this example, 'make_list' is a generator function that yields the double of each number in the range from 0 to 'num'. When we iterate over the generator object returned by this function, we get each number in the sequence one by one.