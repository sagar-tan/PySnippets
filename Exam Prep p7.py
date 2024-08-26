class student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sapid= sap_id
        self.marks = marks
    def display(self):
        print(f"Name:{self.name},SAP ID: {self.sapid}, Marks: {self.marks}")
students=[]
for _ in range (3):
    name = input("Enter Name")
    sapid = input("Enter SAP ID")
    marks = list(map(int, input("Enter Marks of Physics, Chemistry and Maths :").split()))
    Student = student(name, sapid, marks)
    students.append(Student)
for Student in students:
    Student.display()

