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
