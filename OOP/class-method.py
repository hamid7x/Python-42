
class Student:
    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    @classmethod
    def get_count(cls):
        return f"The number of student is {cls.count}"


student1 = Student('Spongebob', 3.4)
student2 = Student('Sandy', 2.0)
student2 = Student('Patrick', 4.4)

print(Student.get_count())
