# Functional Programming in Python

Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. In Python, we can use list comprehensions and set comprehensions as part of the functional programming approach.

List comprehensions are a unique way of quickly creating a list with Python. If you find yourself using a for loop along with .append() to create a list, List comprehensions are a good alternative. 

The syntax for list comprehension is: [expression for item in list]. 

'expression' is the output expression that produces the elements of the new list, and 'item' is the variable that takes on each value in the input sequence 'list'.

Now, let's see an example of list comprehension:

```python
my_list = [item for item in 'hello']
```

Set comprehensions, on the other hand, allow us to create a new set based on an existing set. Here is an example:

```python
my_set = {item for item in 'hello'}