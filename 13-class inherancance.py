class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

a = Animal("Generic Animal")
d = Dog("Tommy")
c = Cat("Kitty")

a.speak()
d.speak()
c.speak()