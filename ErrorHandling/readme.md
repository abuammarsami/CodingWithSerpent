# Error Handling in Python

Error handling in Python is done using try-except blocks. The code that might cause an error is placed inside the 'try' block. If an error occurs, the 'except' block is executed. 

In this example, we are trying to convert the user's input into an integer and perform a division operation. If the user enters a string instead of a number, a ValueError is raised. This is caught and handled by the first 'except' block, which prints a message asking the user to enter a number.

If the user enters '0' as their age, a ZeroDivisionError is raised. This is caught and handled by the second 'except' block.

The 'else' block, which is not shown in this example, would be executed if there were no errors in the 'try' block.

Here is the code:

```python
try:
    age = int(input('What is your age?'))
    10/age
except ValueError:
    print('Please enter a number')
except ZeroDivisionError:
    print('Age cannot be zero')