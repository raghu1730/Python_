print("Entering the values form the keyboard")
name=input("Enter the student name:")
id=input("Enter the student id:")
marks1=input("Enter the Java Marks:")
marks2=input("Enter the Python Marks:")
marks3=input("Enter the C++ marks:")
marks4=input("Enter the Bigdata Marks:")
total = float(marks1) + float(marks2) + float(marks3) + float(marks4)
per= float(total/400 * 100)
print("The name of the student is:",name)
print("The student id is:",id)
print("The total marks of student",name, "is",total)
print("The percentage is", per)
if per >=80 and per <=90:
    print("First Division")
elif per >=70  and per<=79:
    print("Second Divison")
elif per>=60 and per<=69:
    print('Pass')
else:
    print("Fail")

