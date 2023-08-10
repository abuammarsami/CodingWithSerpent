# Concepts of Object Oriented Programming (OOP) in Python
## Table of Contents
- [Introduction](#introduction)
- [What is OOP?](#what-is-oop)
- [Why OOP?](#why-oop)
- [Four Pillars of OOP](#four-pillars-of-oop)
  - [Abstraction](#abstraction)
  - [Encapsulation](#encapsulation)
  - [Inheritance](#inheritance)
  - [Polymorphism](#polymorphism)
  - [Summary](#summary)
  - [References](#references)
  - [Contributors](#contributors)
  - [License](#license)
  - [Appendix](#appendix)
    - [Exploring the Decorator Pattern](#exploring-the-decorator-pattern)
    - [Instance Methods in Python](#instance-methods-in-python)
    - [Static Methods in Python](#static-methods-in-python)
    - [Class Methods in Python](#class-methods-in-python)
    - [Summary](#summary-1)
    - [References](#references-1)
    - [Contributors](#contributors-1)
    - [License](#license-1)
    - [Appendix](#appendix-1)

## Introduction
This article explores the concepts of Object Oriented Programming (OOP) in Python. It is a work in progress, and will be updated as I continue to learn more about OOP. I hope you find it useful!

## What is OOP?
Object Oriented Programming (OOP) is a programming paradigm that relies on the concept of classes and objects. It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes), which are used to create individual instances of objects. There are many object-oriented programming languages including JavaScript, C++, Java, and Python.

## Why OOP?
OOP allows developers to create objects that can be reused within applications. This reduces the amount of code that needs to be written and also makes it easier to understand how a program is built. OOP also makes it possible to create objects that can be used by other developers without having to know how they work internally.

## Four Pillars of OOP
### Abstraction
Abstraction is the process of hiding the internal details and showing only the functionality. Another way, it shows only the essential things to the user and hides the internal details, for example, sending SMS where you type the text and send the message. You don't know the internal processing about the message delivery.

Real-life example: A car is a good example of an abstraction. You don't need to know how the engine works internally but you can still drive the car. You just need to know how to use the steering wheel, pedals, and gear lever.

Code example:
```python
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def drive(self):
        print(f"I am {self.name} and I am driving!")

    def stop(self):
        print(f"I am {self.name} and I am stopping!")

car = Car("BMW", "red")
car.drive()
car.stop()
```
Output:
```
I am BMW and I am driving!
I am BMW and I am stopping!
```
### Encapsulation
Encapsulation is the process of wrapping data and the code that operates on data into a single entity. It is one of the fundamental concepts in object-oriented programming (OOP). Encapsulation is used to hide the values or state of a structured data object inside a class, preventing unauthorized parties' direct access to them. The object is said to be encapsulated because it is wrapped inside a capsule (the class).

Because encapsulation hides the internal workings of an object, it is also called information hiding. Encapsulation is used to protect the integrity of an object's data by preventing unauthorized parties from accessing it directly. It also allows us to change the internal workings of an object without affecting other parts of the program.

Because of encapsulation, we can create objects that are self-contained and independent from each other. This makes it possible to reuse code without having to rewrite it every time we need it. It also makes it easier to understand how a program works because we don't have to know how each object works internally.

Maybe we got a little bit off track here, but the point is that encapsulation is a very important concept in object-oriented programming. It allows us to create objects that are self-contained and independent from each other. This makes it possible to reuse code without having to rewrite it every time we need it. It also makes it easier to understand how a program works because we don't have to know how each object works internally.

Also maybe we can get confused between Abstraction and Encapsulation. Abstraction is the process of hiding the internal details and showing only the functionality. Encapsulation is the process of wrapping data and the code that operates on data into a single entity.

Real-life example: A capsule is a good example of encapsulation. It is a single entity that contains some medicine. You don't know what is inside the capsule but you can still use it to cure your headache.

Code example:
```python
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def drive(self):
        print(f"I am {self.name} and I am driving!")

    def stop(self):
        print(f"I am {self.name} and I am stopping!")

car = Car("BMW", "red")
car.drive()
car.stop()
```
Output:
```
I am BMW and I am driving!
I am BMW and I am stopping!
```
### Inheritance
Inheritance is the process of creating a new class from an existing class. The new class is called a derived class, and the existing class is called a base class. The derived class inherits all the properties and methods of the base class, and it can add new properties and methods to extend the functionality of the base class.

Real-life example: A child is a good example of inheritance. A child inherits all the properties and methods of the parent. The child can also add new properties and methods to extend the functionality of the parent.

Code example:
```python
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def drive(self):
        print(f"I am {self.name} and I am driving!")

    def stop(self):
        print(f"I am {self.name} and I am stopping!")

class BMW(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

    def drive(self):
        print(f"I am {self.name} and I am driving fast!")

car = Car("BMW", "red")
car.drive()
car.stop()
```
Output:
```
I am BMW and I am driving!

I am BMW and I am stopping!
```
### Polymorphism

Polymorphism is the ability of an object to take on many forms. The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object. Any method that is defined in the parent class can be overridden in the child class. This allows us to perform different actions based on the object that we are working with.

Real-life example: A person is a good example of polymorphism. A person can be a student, a teacher, or a parent. A person can also be a son, a daughter, or a sibling.

Code example:
```python
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def drive(self):
        print(f"I am {self.name} and I am driving!")

    def stop(self):
        print(f"I am {self.name} and I am stopping!")

class BMW(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

    def drive(self):
        print(f"I am {self.name} and I am driving fast!")

car = Car("BMW", "red")
car.drive()
car.stop()
```
Output:
```
I am BMW and I am driving!

I am BMW and I am stopping!
```

## Classes and Objects
### Classes
A class is a blueprint for creating objects. It defines the properties and methods that are common to all objects of a certain kind. For example, a Car class might define the properties and methods that are common to all cars, such as the color, model, and year of manufacture. The Car class can then be used to create individual car objects.

### Objects
An object is an instance of a class. It is a concrete entity that exists in memory at runtime. An object can be created by using the new keyword followed by the name of the class. For example, a Car object can be created by using the new keyword followed by the name of the Car class.

## Class and Instance Attributes
### Class Attributes
Class attributes are attributes that are shared by all instances of a class. They are defined outside the constructor method and are accessed using the class name. For example, the Car class has a class attribute called wheels, which is shared by all instances of the Car class.

Code example:
```python
class Car:
    wheels = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def drive(self):
        print(f"I am {self.name} and I am driving!")

    def stop(self):
        print(f"I am {self.name} and I am stopping!")

car = Car("BMW", "red")
print(car.wheels)
```
Output:
```
4
```
### Instance Attributes
Instance attributes are attributes that are unique to each instance of a class. They are defined inside the constructor method and are accessed using the self keyword. For example, the Car class has an instance attribute called name, which is unique to each instance of the Car class.

Code example:
```python
class Car:
    wheels = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def drive(self):
        print(f"I am {self.name} and I am driving!")

    def stop(self):
        print(f"I am {self.name} and I am stopping!")

car = Car("BMW", "red")
print(car.name)
```
Output:
```
BMW
```

## Class and Instance Methods
### Class Methods
Class methods are methods that are shared by all instances of a class. They are defined using the @classmethod decorator and are accessed using the class name. For example, the Car class has a class method called drive, which is shared by all instances of the Car class.

Code example:
```python
class Car:
    wheels = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    @classmethod
    def drive(cls):
        print(f"I am {cls.name} and I am driving!")

    def stop(self):
        print(f"I am {self.name} and I am stopping!")

car = Car("BMW", "red")
car.drive()
```
Output:
```
I am BMW and I am driving!
```
### Instance Methods
Instance methods are methods that are unique to each instance of a class. They are defined inside the constructor method and are accessed using the self keyword. For example, the Car class has an instance method called stop, which is unique to each instance of the Car class.

Code example:
```python
class Car:
    wheels = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    @classmethod
    def drive(cls):
        print(f"I am {cls.name} and I am driving!")

    def stop(self):
        print(f"I am {self.name} and I am stopping!")

car = Car("BMW", "red")
car.stop()
```
Output:
```
I am BMW and I am stopping!
```

