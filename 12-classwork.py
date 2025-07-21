Python Classes with Examples
1. Basic Class and Object
class Dog:
    def bark(self):
        print("Woof! Woof!")

dog1 = Dog()
dog1.bark()  # Output: Woof! Woof!
2. Constructor (__init__) and Instance Variables
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

p1 = Person("Sahitya", 25)
p1.intro()
3. Class Variables & Static Methods
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius * self.radius

    @staticmethod
    def greet():
        print("I am a circle!")

c = Circle(5)
print(c.area())
Circle.greet()
4. Inheritance
class Animal:
    def sound(self):
        print("This is some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")

d = Dog()
d.sound()
5. Encapsulation (Private Variables)
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(5000)
print(account.get_balance())
6. Polymorphism (Method Overriding)
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

s = Square(4)
print(s.area())
7. Property Decorators (Getters and Setters)
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name.upper()

    @name.setter
    def name(self, value):
        self._name = value

s = Student("Sahitya")
print(s.name)
s.name = "Karn"
print(s.name)
