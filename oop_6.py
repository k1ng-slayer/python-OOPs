"""
Property Decorators - Getters, Setters, and Deleters
"""


class Employee:

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        # self.email = first.lower() + '.' + last.lower() + '@fcb.com'

    # to make it seem like an attribute yet reflect the changes
    @property
    def email(self):
        return f'{self.fname.lower()}.{self.lname.lower()}@fcb.com'

    @property
    def fullname(self):
        return self.fname + ' ' + self.lname

    # setter method
    @fullname.setter
    def fullname(self, name):
        self.fname, self.lname = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Ilkay', 'Gundogan', 100)
emp_2 = Employee('Inigo', 'Martinez', 25)
# print(emp_2.fullname())
# print(emp_2.email)

# emp_2.fname = 'Lisandro'
# print(emp_2.fullname())
# # here we notice that the email-id isnt changing with the changing fname(before declaring @property)
# print(emp_2.email)

# we cannot set the name of 'emp_1' without using the setter method
emp_1.fullname = 'Lionel Messi'
print(emp_1.fname)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
