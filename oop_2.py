"""
Class Variables
"""


class Employee:

    # class variables
    raise_amount = 1.15
    num_employee = 0

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@fcb.com'

        # the value of 'num_employee' will be incremented every time an instance of the class is created (instansiated)
        Employee.num_employee += 1

    def fullname(self):
        return self.fname + ' ' + self.lname

    def apply_raise(self):
        self.pay = f"{int(self.pay * self.raise_amount)}k/week"


print(Employee.num_employee)
emp_1 = Employee('Ilkay', 'Gundogan', 100)
emp_2 = Employee('Inigo', 'Martinez', 25)
print(Employee.num_employee)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# # we can access the variable raise_amount even tho its not declared inside the method
# print(Employee.__dict__)
# print(emp_1.__dict__)

# changes the value of 'raise_amount' for every instance of that class
# Employee.raise_amount = 1.25
# changes the value of 'raise_amount' for only that instance of that class ('emp_1')
# emp_1.raise_amount = 1.75

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
