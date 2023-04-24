#define a class
class Student:
    name=""
    id=0

    #create object of the class
std = Student()   # Student std = new Student() in java object

#access attibutes and assign new values
std.id=6250
std.name="John"
print(f"Name:{std.name}, id:{std.id}")
