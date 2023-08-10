#Our customize error handling.

# Syntax:
#         try:
#                 codes that might cause an error.
#         except:
#                 codes that will run if there is an error.
#         else: # if there is no error in try block. else block will be executed.
#                 codes that will run if there is no error.
#         finally: # finally block will always be executed.
#                 codes that will run no matter what.

try:
    age = int(input('What is your age?'))
    10/age
    print(f'Your age is {age}.')
except ValueError: # This will catch any error that is not ZeroDivisionError
    print(f'Your entered input for age  is not a number. Please enter a Number')
except ZeroDivisionError: # This will catch ZeroDivisionError
    print(f'Your age can\'t be 0, please be concious')

else: # if there is no error in try block. else block will be executed.
    print('Thank you :)')

