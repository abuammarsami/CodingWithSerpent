#
# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print(f'Please enter numbers {err}')
#
#
# sum(1, '1')


def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'The exception is {err}')


sum(1, 'asdasd')