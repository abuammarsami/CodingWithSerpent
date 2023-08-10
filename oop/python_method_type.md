# The 3 Types of Methods in Python

In Python, there are three types of methods: instance methods, static methods, and class methods. While you may not need to distinguish between these methods in every basic Python script, understanding their differences becomes crucial when employing Object-Oriented Programming (OOP) for more advanced code.

## Exploring the Decorator Pattern

Before diving into the differences, it's essential to grasp the decorator pattern, a design pattern that Python employs for defining static or class methods. Decorators, which are simply functions, modify the behavior of other functions and help segregate logic into distinct concerns. This pattern enhances code reuse and separation.

The decorator pattern is Python's recommended way to define static or class methods. Below is an example of a decorator in Python:

```python
class DecoratorExample:
    """ Example Class """
    def __init__(self):
        """ Example Setup """
        print('Hello, World!')

    @staticmethod
    def example_function():
        """ This method is decorated! """
        print('I\'m a decorated function!')
```
Decorators have to immediately precede a function or class declaration. They start with the @ sign, and unlike normal methods, you don't have to put parentheses on the end unless you are passing in arguments.

It's possible to combine decorators, write your own, and apply them to classes as well, but you won't need to do any of that for these examples.

## Instance Methods in Python
Instance methods are the most common type of methods in Python classes. These are so-called because they can access unique data of their instance. If you have two objects each created from a car class, then they each may have different properties. They may have different colors, engine sizes, seats, and so on.

Instance methods must have self as a parameter, but you don't need to pass this in every time. Self is another Python special term. Inside any instance method, you can use self to access any data or methods that may reside in your class. You won't be able to access them without going through self. However, on top of self, you can include other parameters as well.

Finally, as instance methods are the most common, there's no decorator needed. When you create a Python class, its methods will be instance methods by default.

Here's an example:

```python
class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!')
    self.name = 'Decorator_Example'
 
  def example_function(self):
    """ This method is an instance method! """
    print('I\'m an instance method!')
    print('My name is ' + self.name)
 
de = DecoratorExample()
de.example_function()
```
The name variable is accessed through self. Notice that, when you call example_function, you don't have to pass self in—Python does this for you.

## Static Methods in Python
Static methods are methods that don't have access to any data or methods that reside in a class. They are self-contained and don't depend on an instance or class. They are present in a class because it makes sense for them to be present in a class.
So, why would you use static methods? They are useful for grouping methods that have some logical connection to a class to the class. They improve code organization and readability.
You can define a static method with the @staticmethod decorator. Here's an example:

```python
class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!')
    self.name = 'Decorator_Example'
 
  def example_function(self):
    """ This method is an instance method! """
    print('I\'m an instance method!')
    print('My name is ' + self.name)
 
  @staticmethod
  def example_static_method():
    """ This method is a static method! """
    print('I\'m a static method!')
DecoratorExample.example_function()
```
Notice that you don't have to pass self in as a parameter. Static methods are self-contained and don't have access to any data or methods that reside in a class.

## Class Methods in Python
Class methods are methods that have access to the class itself as an object. They don't have access to any instance of that class. They are present in a class because it makes sense for them to be present in a class.

Class methods are similar to static methods, but they are different in that they have access to the class itself. They are useful for grouping methods that have some logical connection to a class to the class. They improve code organization and readability.

You can define a class method with the @classmethod decorator. Here's an example:

Class methods know about their class. They can't access specific instance data, but they can call other static methods.

Class methods don't need self as an argument, but they do need a parameter called cls. This stands for class, and like self, it gets automatically passed in by Python.

```python
class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Hello, World!')
    self.name = 'Decorator_Example'
 
  def example_function(self):
    """ This method is an instance method! """
    print('I\'m an instance method!')
    print('My name is ' + self.name)
 
  @staticmethod
  def example_static_method():
    """ This method is a static method! """
    print('I\'m a static method!')
 
  @classmethod
  def example_class_method(cls):
    """ This method is a class method! """
    print('I\'m a class method!')
    print('My name is ' + cls.__name__)

DecoratorExample.example_class_method()
```
Notice that you don't have to pass self in as a parameter. Class methods are self-contained and don't have access to any data or methods that reside in an instance of a class. However, they do have access to the class itself.

Remember, instance methods can manipulate an object's state and have access to the class itself via self. Class methods, on the other hand, can't access the instance of a class but can access the class itself. This is the major difference between class and instance methods in Python.

Since class methods can manipulate the class itself, they are useful when you're working on larger, more complex projects.


## Conclusion
In this article, you learned about the three types of methods in Python: instance methods, static methods, and class methods. You also learned about the decorator pattern, which is Python's recommended way to define static or class methods. Finally, you learned about the differences between these three types of methods.

