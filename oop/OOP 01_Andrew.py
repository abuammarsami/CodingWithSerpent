# By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class.
class Toy:
    classVar = "Hi I am a class variable"

    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }
        self.instanceAttribute = None

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return ('yes??')

    def __getitem__(self, i):
        return self.my_dict[i]

    @classmethod
    def play(cls):
        print("playing with " + cls.classVar)

    @staticmethod
    def attack():
        print("attacking with " + Toy.classVar)

    @staticmethod
    def play_like_class_variable(cls):
        print("playing with " + cls.classVar)


action_figure = Toy('red', 0)
action_figure.attackInMain = "Dhishum Dhishum"
Toy.play()  # Toy.play() is Class Method that's why we don't have to pass the class as parameter
Toy.attack()
action_figure.attack() # we can also call static method with object
Toy.play_like_class_variable(Toy) # Toy.play_like_class_variable() is Static Method that's why we have to pass the
# class as parameter
print("\n===================***********========================\n")
print(action_figure.attackInMain)
print(action_figure.__str__()) # __str__() is used to print the object as string
print(str(action_figure))  # __str__() is used to print the object as string
print(len(action_figure))   # __len__() is used to get the length of the object
print(action_figure())  # __call__() is used to call the object as function
print(action_figure['name'])  # __getitem__() is used to get the value of the key from the dictionary
help(Toy)

class Panda(Toy):
    def __init__(self, color, age, name):
        # Toy.__init__(self, color, age) # Toy.__init__() is used to call the parent class constructor, and we have to pass self
        super().__init__(
            color, age
        )  # super() is used to call the parent class constructor, and we don't have to pass self
        self.name = name

    def __str__(self):
        return f"{self.color} {self.name}"


