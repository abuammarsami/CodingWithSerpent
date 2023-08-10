# Error Handling

# age = int(input('What is your age? '))
#
# print(age)

"""
Write an error handling for this case. If the user enters a string instead of an integer, the program will crash.  

Syntax:
        try: 
                codes that might cause an error. 
                
        except: 
                codes that will run if there is an error. 
                
        else: # if there is no error in try block. else block will be executed. 
                codes that will run if there is no error.   
                
"""

while True:
    try:
        age = int(input('What is your age?'))
        10/age
        print(f'Your age is {age}.')
    except ValueError:
        print(f'Your entered input for age  is not a number. Please enter a Number')

    except ZeroDivisionError:
        print(f'Your age can\'t be 0, please be concious')

    else:
        print('Thank you :)')
        break

