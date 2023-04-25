class Student:  # class Name
    def std_grade(self):  # method
        if self.marks>=60:
            return True
        else:
            return False
std1 = Student() # 1st object creation Student std1 = new Student()
std1.name=input("Enter the Student Name:")
std1.marks=float(input("Enter the student marks:"))

std_pass1 = std1.std_grade() # object to method name declared to variable
print(std_pass1)  # print statements
print(std1.name)  # print statements
print(std1.marks)  # print statements

std2 = Student()   # 2nd object creation
std2.name=input("Enter the Student Name:")
std2.marks=float(input("Enter the student marks:"))

std_pass2 = std2.std_grade()
print(std_pass2)
print(std2.name)
print(std2.marks)

