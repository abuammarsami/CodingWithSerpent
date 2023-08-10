# list comprehension, set comprehension, dictionary comprehension

# list comprehension - creates a new list based on another list
print('\nlist comprehension')
# new_list = [new_item for item in list]

my_list = []

for item in 'hello':
    my_list.append(item)

print(my_list)

"""
In other programming language you would have to write a for loop to create a new list based on another list. 
In python you can use list comprehension to do this in one line of code.

syntax:
        new_list = [params for params in iterable : optional if statement]

"""

my_list = [item for item in 'hello']
print(my_list)

my_list2 = [num for num in range(0, 100)]
print(my_list2)

my_list3 = [num ** 2 for num in range(0, 100)]
print(my_list3)

my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(my_list4)

# set comprehension - creates a new set based on another set.
print('\nset comprehension')
# new_set = {new_item for item in set}

my_set = {item for item in 'hello'}
print(my_set)  # {'l', 'o', 'e', 'h'}--> as set returns only unique values. So it will not return 'h' twice.

my_set2 = {num for num in range(0, 100)}
print(my_set2)

my_set3 = {num ** 2 for num in range(0, 100)}
print(my_set3)

my_set4 = {num ** 2 for num in range(0, 100) if num % 2 == 0}
print(my_set4)

# dictionary comprehension - creates a new dictionary based on another dictionary
print('\ndictionary comprehension')
# new_dict = {new_key:new_value for key, value in dict.item()}

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict2 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict2)

# Exercise
print('\nExercise')
"""
1. Create a list of numbers from 1 to 100
2. Create a list of even numbers from 1 to 100
3. Create a list of odd numbers from 1 to 100
4. Create a list of numbers from 1 to 100 that are divisible by 3
5. Create a list of numbers from 1 to 100 that are divisible by 5
6. Create a list of numbers from 1 to 100 that are divisible by 3 and 5
7. Create a list of numbers from 1 to 100 that are divisible by 3 or 5
8. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both
9. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are even
10. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are odd
11. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are even and are divisible by 4
12. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are odd and are divisible by 4
13. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are even and are divisible by 4 
and are divisible by 6.
14. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are odd and are divisible by 4.
15. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are even and are divisible by 4.
16. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are odd and are divisible by 4.
17. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are even and are divisible by 4.
18. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are odd and are divisible by 4.
19. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are even and are divisible by 4.
20. Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both and are odd and are divisible by 4.
"""