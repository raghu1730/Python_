# Inherits, extends and override
# Multiple Interitance using python
class Employee:  # parent class or super class or base class
    #instance attributes
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def work(self):
        print(f"{self.name} is working in TCS")
class SoftwareEngineer(Employee):
    def __init__(self, name,age,salary, level):
        super().__init__(name, age, salary)
        self.level = level
    def work(self):
        print(f"{self.name} is working in Goodle")
    def debug(self):
        print(f"{self.name} is debugging")
class Designer(Employee):   # subclass or child class
    def work(self):
        print(f"{self.name} is working in amazon")
    def draw(self):
        print(f"{self.name} is drawing")
#instance
se= SoftwareEngineer("John",25, 5000, "Junior")
print(se.name, se.age, se.salary)
#se2 = SoftwareEngineer("David", 28, 4000, "Senior")
se.work()
#se2.work()
d=Designer("David", 28, 4000)
print(d.name, d.age, d.salary)
d.work()
d.draw()