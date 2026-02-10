class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@comany.com"
        self.salary = salary

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee("jhon", "smith", 50000)
print(emp1.fullname())
print(emp1.email)
