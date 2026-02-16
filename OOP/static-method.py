
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ['Manager', 'Cook', 'Cashier']
        return position in valid_position


emp1 = Employee('Spongebob', 'Cook')
emp2 = Employee('Eugune', 'Manager')
emp3 = Employee('Squidward', 'Cashier')

print(Employee.is_valid_position('Cook'))  # True
print(Employee.is_valid_position('Rocket Scientist'))  # False

print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())
