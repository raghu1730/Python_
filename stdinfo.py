class Student:
    def stdgradedetail(self):
        self.std_id=input("Enter the student Id:")
        self.name=input("Enter the student Name:")
        self.bigdata=float(input("Enter the BigData Marks:"))
        self.java=float(input("Enter the Java Marks:"))
        self.python=float(input("Enter the Python Marks:"))
        self.stat=float(input("Enter the Statistics Marks:"))

    def stdpercentage(self):
        self.total=(self.java + self.bigdata +self.stat + self.python)
       # print("The total marks of", self.name,"is",self.total)
        self.per = (self.total/400 * 100)
        print("The Percentage of", self.name, "is", self.per)
    def stdgrades(self):
        if std.per >=60:
            print("Student Pass")
        else:
            print("Student Failed")
std = Student()
print(std.stdgradedetail())
print("--- Result---")
print(std.stdpercentage())
print(std.stdgrades())