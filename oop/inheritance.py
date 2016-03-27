class Person:

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def __str__(self):
        return self.first_name + " " + self.last_name

class Employee(Person): #inherits from Person

    def __init__(self, first, last, staff_num):
        super().__init__(first, last)
        self.staff_number = staff_num

    def __str__(self):
        return super().__str__() + ", " + self.staff_number

person = Person("John", "Smith")
employee = Employee("Homer", "Simpson", "1007")

print("Person: " + str(person))
print("Employee: " + str(employee))
