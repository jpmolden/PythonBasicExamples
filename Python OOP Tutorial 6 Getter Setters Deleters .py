

## __ is dunder - Double Under
## .
import datetime

class OurClass:

    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        print("Returning the private attrute from the property decoated funtion")
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        print("Using the property decorted setter")
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


class Company:
    comp_name = "MyCompany"

class Employee(Company):
    #class attribute
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.startDate = datetime.date(2016,11,12)
        # Replace with property decorator
        #self.email = first + '.' + last + '@' + self.comp_name + '.com'

    # Property decorator define a method that allows access like an attribute ie print(email)
    @property
    def email(self):
        return self.first + '.' + self.last + '@' + self.comp_name + '.com'

    #instance methods
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.first)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name")
        self.first = ''
        self.last = ''


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    # Dunder/Magic implicitly called when we repr(object)
    # Used for debug/logging
    def __repr__(self):
        return "repr Employee(first'{}', last'{}', pay'{}', email:'{}')".format(self.first, self.last, self.pay, self.email)
    # Dunder/Magic implicitly called when we str(object)
    # Readable for end user
    def __str__(self):
        return "Str Employee(first'{}', last'{}', pay'{}', email:'{}')".format(self.first, self.last, self.pay, self.email)

    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return

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
    # dev1 = Developer('Corey', 'Mills', 20000, 'Python')
    #
    # dev2 = Developer('Test', 'Employee', 20000, 'Java')
    #
    # mngr1 = Manager('sue','smith',90000,[dev1])
    #
    # jan1 = Janitor('Steve', 'Mills', 100, 'OlRusty')
    #
    # emp1 = Employee('An', 'empplotess',4564)
    #
    # emp1.fullname = 'New Fullname'
    # print(emp1)
    # del emp1.fullname
    # print(emp1)

    print("Init oc")
    oc = OurClass(7)
    print("print(oc.__OurAtt)")
    # print(oc.__OurAtt)
    # print("print(oc.OurAtt)")
    print(oc.__dict__)
    print(repr(oc))

if __name__ == '__main__':
    print("Run Msain")
    main()
