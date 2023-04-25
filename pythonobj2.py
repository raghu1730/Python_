class Student:
    def std_grade(self):
        if self.marks>=60:
            return True
        else:
            return False
    def __init__(self, name,marks): # like a constructor in java
        self.name = name
        self.marks = marks
name = input("Enter the student name:")
marks = float(input("Enter the marks:"))
std1 = Student(name,marks)
print(std1.name)
print(std1.marks)
print(std1.std_grade())