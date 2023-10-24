class Student:
    attending = 0

    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree
        Student.attending = Student.attending + 1

    def change_name(self, name):
        self.name = name


Michael = Student("Michael", 21, "Business Management")
Ramon = Student("Ramon", 21, "Information Technology")
Jill = Student("Jill", 24, "MedTech")
Student.change_name(Michael, "Bill")

print(f"There are {Student.attending} students attending this class")
print(f"{Michael.name,Michael.age,Michael.degree}")