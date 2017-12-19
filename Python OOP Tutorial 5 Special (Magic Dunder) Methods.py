

## __ is dunder - Double Under
## .
import datetime

class Company:
    comp_name = "XYZ Corp"

class Employee(Company):
    #class attribute
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.startDate = datetime.date(2016,11,12)

    #instance methods
    def fullname(self):
        return '{} {}'.format(self.first,self.first)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    # Dunder/Magic implicitly called when we repr(object)
    # Used for debug/logging
    def __repr__(self):
        return "repr Employee(first'{}', last'{}', pay'{}')".format(self.first, self.last, self.pay)
    # Dunder/Magic implicitly called when we str(object)
    # Readable for end user
    def __str__(self):
        return "Str Employee('first {}', last'{}', pay'{}')".format(self.first, self.last, self.pay)

    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.first)

#Developer inherits from Employee class above
class Janitor(Employee):
    raise_amt = 1.30
    def __init__(self, first, last, pay, fav_mop):
        super().__init__(first, last, pay)


class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        ##Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []  ##Empty list
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def print_emps(self):
        print('Employees List')
        for emp in self.employees:
            print('-->', emp.first)


##print(help(Developer)) #Print developer method resolution order
##print(dev1.pay)
##dev1.apply_raise()
##print(dev1.pay)

def main():
    dev1 = Developer('Corey', 'Mills', 20000, 'Python')

    dev2 = Developer('Test', 'Employee', 20000, 'Java')

    mngr1 = Manager('sue','smith',90000,[dev1])

    print(dev1.prog_lang)
    dev1.apply_raise()
    print(dev1.pay)

    mngr1.print_emps()
    print(dev1.pay)

    jan1 = Janitor('Steve', 'Mills', 100, 'OlRusty')

    mngr1.add_emp(jan1)
    mngr1.print_emps()

    mngr2 = Manager('sue','smith',90000)
    mngr2.print_emps()

    print("Printing mngr1")
    print(mngr1)
    print(repr(mngr1))
    print(str(mngr1))

    print("New Employee Test")
    newEmp = Employee('New', 'Emp', 45654)
    print(newEmp)
    print(repr(newEmp))
    print(str(newEmp))

    print("Using dunder to add new functions")
    print(dev1 + mngr1)

    print("Using the employees parent class")
    print(dev1.comp_name)
    print(mngr1.comp_name)


    print(int.__add__(1,2))
    print(dev1 + dev2)
    print(len(dev1))

if __name__ == "__main__":
    print("Run Main")
    main()
