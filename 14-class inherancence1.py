class Calculator:
    def __init__(self, name):
        self.name = name
    
    def add(self, a, b):
        return a + b
    
    def display_info(self):
        print(f"{self.name} calculator")

class ScientificCalculator(Calculator):
    def add(self, a, b):
        result = super().add(a, b)
        print(f"Scientific calculation: {a} + {b} = {result}")
        return result
    
    def add_multiple(self, *numbers):
        total = 0
        for num in numbers:
            total = self.add(total, num)
        return total

class AdvancedCalculator(Calculator):
    def __init__(self, name, precision):
        super().__init__(name)
        self.precision = precision
    
    def add(self, a, b):
        result = super().add(a, b)
        return round(result, self.precision)
    
    def add_with_history(self, a, b):
        result = self.add(a, b)
        print(f"Added {a} + {b} = {result} (precision: {self.precision})")
        return result

basic_calc = Calculator("Basic")
sci_calc = ScientificCalculator("Scientific")
adv_calc = AdvancedCalculator("Advanced", 2)

basic_calc.display_info()
print(f"Basic addition: {basic_calc.add(5, 3)}")

sci_calc.display_info()
sci_calc.add(10, 7)
print(f"Multiple addition: {sci_calc.add_multiple(1, 2, 3, 4, 5)}")

adv_calc.display_info()
adv_calc.add_with_history(3.567, 2.789)