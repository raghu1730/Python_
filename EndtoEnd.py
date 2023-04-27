# class, instance, methods end-to-end
std1 = ["CSA", "John", 25, "Montreal", "john@gmail.com"]
std2 = ["ABD","David", 26, "Toronto", "david@yahoo.com"]
class TrebasCollege:
      #constructor
    def __init__(self, course, name, age, address, emailid):
        #instance attributes
        self.course = course
        self.name = name
        self.age = age
        self.address = address
        self.emailid = emailid
        #instance method
    def stdinfo(self):
        print(f"{self.name} is studying in {self.course}")
    def programlanguage(self, language):
        print(f"{self.name} is coding in {language}")
    def std_age(self, age):
          if age < 25:
            return 5000
          if age < 27:
              return 7000
          else:
              return 8000
# instance
tc1 = TrebasCollege("CSA","John", 25 ,"Montreal", "john@gmail.com")
tc2 = TrebasCollege("ABD","David", 26, "Toronto", "david@yahoo.com")
tc1.stdinfo()#method calling using instance
tc2.stdinfo()
tc1.programlanguage("Python")#passing arguments from method
tc2.programlanguage("Java")
print(TrebasCollege.std_age(26))
#print(tc1.name, tc1.course)

