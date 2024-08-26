class student:
    def __init__(self, name, stud_id, math, science, eng):
        self.name = name
        self.id=stud_id
        self.grades = {'Math':math, 'Science':science, 'English':eng}
    def average_grade(self):
        return sum(self.grades.values())//len(self.grades)
Students = [
    student("Alice", 1, 85, 90, 88), 
    student("Bob", 2, 78, 82, 80), 
    student("Charlie", 3, 92, 95, 91)
    ]
Students.sort(key=lambda student:student.average_grade())
for student in Students:
    print(f"{student.name}, ID:{student.id}, avg. grade: {student.average_grade()}")
