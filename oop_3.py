"""
classmethods & staticmethods
"""


import datetime


class Employee:

    raise_amount = 1.15
    num_employee = 0

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@fcb.com'

        Employee.num_employee += 1

    # these are 'regularmethods' as they automatically take the instacnce 'self' as their first argument
    def fullname(self):
        return self.fname + ' ' + self.lname

    def apply_raise(self):
        self.pay = f"{int(self.pay * self.raise_amount)}k/week"

    # creating a 'classmethod' (alternative constructors)
    # class is the first default argument, written as 'cls' because keyword 'class' is already used when declaring 'class Employee'
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # return Employee(first, last, pay)
        return cls(first, last, pay)

    # creating a 'staticmethod'
    # they do not have any automatic argument(like 'self'/'cls')
    # they behave just like regular functions
    # use a 'staticmethod' when you dont access the instance or class within the function
    @staticmethod
    def is_workday(day):
        if day.weekday() == 6 or day.weekday == 7:
            return False
        return True


emp_1 = Employee('Ilkay', 'Gundogan', 100)
emp_2 = Employee('Inigo', 'Martinez', 25)

"""
print(Employee.raise_amount)
print(emp_1.raise_amount)

Employee.set_raise_amt(1.35)

# running 'classmethod' from the instance also changes the value of class variable
# emp_1.set_raise_amt(1.35)

print(Employee.raise_amount)
print(emp_1.raise_amount)
"""

"""
str_emp_3 = 'Vitor-Roque-10'
str_emp_4 = 'Joshua-Kimmich-50'
str_emp_5 = 'Arda-Guller-25'

emp_3 = Employee.from_string(str_emp_3)
print(emp_3.email)
"""


my_date = datetime.date(2023, 7, 3)
print(Employee.is_workday(my_date))
