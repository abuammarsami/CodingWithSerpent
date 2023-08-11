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
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
help(Toy)
