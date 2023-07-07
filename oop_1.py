"""
Classes & Instances
"""


# empty class
class Empty:
    pass


# this is a class
class Employee:

    # method to initialize OR constructor method.
    # 'self' is received as an automatic first argument
    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@fcb.com'

    # creating a method within the class
    # method is a function associated with a class
    # each method in a class will automatically take in the instance as its first argument
    def fullname(self):
        # instead of writing 'emp_1.fname' we write 'self.fname' and so on
        return self.fname + ' ' + self.lname


# these are instances of a class
emp_1 = Employee('Ilkay', 'Gundogan', 100)


print('Class Instance: ', emp_1)
print('Email of class instance:', emp_1.email)

# print(emp_1.fname + ' ' + emp_1.lname)
# instead of passing on these expressions in print statements, we can create a method fullname() in the class
print(emp_1.fullname())
# does the same thing
print(Employee.fullname(emp_1))
