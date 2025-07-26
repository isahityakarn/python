# class Dog:
#     def sound(self):
#         print("Woof! Woof!")
#     def eat(self, food):
#         print(f"The dog is eating {food}.")
# dog1 = Dog()
# dog1.sound()
# dog1.eat("meat")

class Calculator:
    def __init__(self):
        self.value = 5
    def add(self, amount,amount1):
        self.value = amount + amount1
        return self.value
       

    def subtract(self, amount):
        self.value -= amount
        return self.value

    def multiply(self, factor):
        self.value *= factor
        return self.value

    def divide(self, divisor):
        if divisor != 0:
            self.value /= divisor
            return self.value
        else:
            raise ValueError("Cannot divide by zero")
cal = Calculator()
print(cal.add(5,15))
print(cal.subtract(3))
print(cal.multiply(2))
print(cal.divide(4))
# cal.divide(0)     # Raises ValueError: Cannot divide by zero