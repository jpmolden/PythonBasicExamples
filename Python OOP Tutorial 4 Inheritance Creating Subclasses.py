class Employee:
    #class attribute
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    #instance methods
    def fullname(self):
        return '{} {}'.format(self.first,self.first)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

#Developer inherits from Employee class above
class Janitor(Employee):
    raise_amt = 1.30
    def __init__(self, first, last, pay, fav_mop):
        super().__init__(first, last, pay)


class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
##        Employee.__init__(self, first, last, pay)
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

dev1 = Developer('Corey', 'Mills', 20000, 'Python')

dev2 = Developer('Test', 'Employee', 20000, 'Java')

mngr1 = Manager('sue','smith',90000,[dev1])

##print(help(Developer)) #Print developer method resolution order
##print(dev1.pay)
##dev1.apply_raise()
##print(dev1.pay)

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
