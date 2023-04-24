# define a class
class Employee:
    # define an attributes
    employee_id=0
    emp_name=""
    emp_salary=0
    Hr_sal=50
    Total_hr=30
    name=""
    #method to calculate the salary of employee
    def salary_calculate(self):  #public string employee(string name) in java
        print("The salary of employee is:",self.Hr_sal * self.Total_hr)
#create two object for the employee class
employ1 = Employee()
employ2 = Employee()
# access attributes using employee
employ1.employee_id=1010
print(f"Employee Id is: {employ1.employee_id}")
employ2.emp_name="John"
print(f"Employee Name is: {employ2.emp_name}")
employ1.salary_calculate()
