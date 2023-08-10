Digit_To_Word = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

Phone_Number = input("Enter Phone NUmber: ")
Convert_Number = ""
for digit in Phone_Number:
    Convert_Number += Digit_To_Word.get(digit) + " "
    
print(Convert_Number)


# find prime numbers
# prime numbers are numbers that are only divisible by 1 and itself. 1 is not a prime number. 2 is a prime number.

# for number in range(1, 101):
#     if number > 1:
#         for i in range(2, number):
#             if (number % i) == 0:
#                 break
#         else:
#             print(number)

def find_Prime_number(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)