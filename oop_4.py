"""
Inheritence - Creating Subclasses
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


# inheriting from 'class Employee'
class Developer(Employee):
    raise_amount = 1.60

    # to add attributes in addition to the parent class' attribute we can give the inherited class its own '__init__' method
    def __init__(self, first, last, pay, style):
        # parent class will handle the 'first', 'last' & 'pay' attributes
        # M1
        super().__init__(first, last, pay)
        # M2
        # Employee.__init__(self, first, last, pay)
        self.style = style


# inheriting from 'class Employee'
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # method to add an employee
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # method to remove an employee
    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # method to return all the employees
    def ret_emps(self):
        count = 1
        for x in self.employees:
            print(f'{count})', x.fullname())
            count = count + 1


emp_1 = Employee('Ilkay', 'Gundogan', 100)
emp_2 = Employee('Inigo', 'Martinez', 25)

dev_1 = Developer('Marc-Andre', 'Ter Stegen', 100, 'Offensice Goalkeeper')
dev_2 = Developer('Ronald', 'Araujo', 15, 'Destroyer')

# print(help(Developer))

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_2.email)
# print(dev_2.style)

mgr_1 = Manager('Xavi', 'Hernandez', 200, [dev_1])
# print(mgr_1.email)
# print(mgr_1.ret_emps())
# mgr_1.add_emp(dev_2)
# print(mgr_1.ret_emps())
# mgr_1.rem_emp(dev_1)
# print(mgr_1.ret_emps())

# isinstance() & issubclass() functions can be used to find out if an object is an instance or class, respectively of a class

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
