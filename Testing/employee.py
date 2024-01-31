class Employee:
    """ Stores information about an employee """

    def __init__(self, first, last, position, salary):
        """ Store the employee's name, position, and salary """
        self.first = first
        self.last = last
        self.position = position
        self.salary = salary
        self.full_name = f"{first} {last}"

    def __str__(self):
        """ Return a string representation of the employee """
        return f"{self.full_name} \n{self.position} \n{self.salary}"

    def give_raise(self, amount=5000):
        """ Give the employee a raise """
        self.salary += amount
        return self.salary
    
employee_1 = Employee('John', 'Doe', 'Software Engineer', 143600)
employee_2 = Employee('Jane', 'Doe', 'Data Scientist', 130100)
employee_3 = Employee('Jim', 'Wrangler', 'DevOps Engineer', 135000)
employees = [employee_1, employee_2, employee_3]

print()
for employee in employees:
    print(employee)
    print()

employee_1.give_raise(10000)
employee_2.give_raise(-10000)
print(employee_1)
print(employee_2)