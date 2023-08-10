# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
doraemon = Cat("Doraemon", 1000)
tom = Cat("Tom", 10)
oggy = Cat("Oggy", 10)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest_cat(doraemon.age, tom.age, oggy.age)} years old.")


# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat_1 = Cat('boris', 10)
cat_2 = Cat('meow', 7)
cat_3 = Cat('cc', 2)


# 2 Create a function that finds the oldest cat
def find_oldest_cat(cats):
    return max(cats, key=lambda cat: cat.age)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
oldest_cat = find_oldest_cat((cat_1, cat_2, cat_3))
print(f'The oldest cat is {oldest_cat.age} years old.')
