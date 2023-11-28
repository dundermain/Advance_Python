#attributes and methods can have different level of encapsulation like
#1. public methods/attributes: can be accessed by subclass or outside the class using dot niotation
#2. private methods/attributes: cannot be accessed by subclass or outside the class. We need to put in getter setter methods to access it
#3. protected methods/attributes: cab be used by subclass or outside the class but with a warning

#public attribute
class MyClass:
    def __init__(self):
        self.public_attribute = 10

obj = MyClass()
print(obj.public_attribute)  # Accessing public attribute


#protected attribute
class MyClass:
    def __init__(self):
        self._protected_attribute = 20

obj = MyClass()
# Accessing protected attribute (not recommended)
print(obj._protected_attribute)


#private attribute
class MyClass:
    def __init__(self):
        self.__private_attribute = 30

obj = MyClass()
# This will result in an AttributeError
# print(obj.__private_attribute)
