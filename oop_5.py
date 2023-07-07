"""
Special (Magic/Dunder) Methods
"""


class Employee:

    raise_amount = 1.15

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@fcb.com'

    def fullname(self):
        return self.fname + ' ' + self.lname

    def apply_raise(self):
        self.pay = f"{int(self.pay * self.raise_amount)}k/week"

    # dunder methods
    def __repr__(self):
        return f"Employee('{self.fname}', '{self.lname}', '{self.pay}')"

    def __str__(self):
        return f"{self.fullname} => {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Ilkay', 'Gundogan', 100)
emp_2 = Employee('Inigo', 'Martinez', 25)

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

# if we say add Employee_1 & Employee_2, it will mean we have to add the pay of both the employees which is defined bt "__add__"
# print(emp_1 + emp_2)

# print(len('abcd'))
# print('abcd'.__len__())

print(len(emp_1))
