# Static method

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager","Cahier","Cook","Janitor"]
        return position in valid_positions
    
employee1 = Employee("Eugene", "Janitor")
employee2 = Employee("Tom", "Cashier")
employee3 = Employee("Daniel", "Cook")

# print(Employee.is_valid_position("Cook"))
# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())


# Class method

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    

student1 = Student("Ralph", 3.4)
student2 = Student("Sam", 4.3)
student1 = Student("Timmy", 2.4)

# print(Student.get_count())
# print(Student.get_average_gpa())

    

    










