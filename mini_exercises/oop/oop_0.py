# Object Oriented Programming in Python


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def remove_student(self, student):
        if student in self.students:
            print(f"# Removing {student.name} #")
            self.students.remove(student)
            return f"'{student}' removed"
        else:
            return f"Student '{student.name}' is not part of the '{self.name}' course"

    def get_average_grade(self):
        if not self.students:
            return 0.0
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Nick", 19, 97)
s2 = Student("Henry", 19, 78)
s3 = Student("Anna", 19, 57)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)

for student in course.students:
    print(student.name)

print(course.remove_student(s1))
for student in course.students:
    print(student.name)

course.add_student(s3)

print("Average: ", course.get_average_grade())
