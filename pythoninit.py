class Employee:
    def __init__(self, emp_name):
        self.emp_name = emp_name

        # Sample method
    def emp_detail(self):
        print("Employee name is:",self.emp_name)
emp_obj = Employee("John")
emp_obj.emp_detail()