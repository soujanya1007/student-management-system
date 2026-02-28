class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"\nName: {self.name}")
        print(f"Roll No: {self.roll}")
        print(f"Marks: {self.marks}")

students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        marks = input("Enter Marks: ")
        students.append(Student(name, roll, marks))
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                student.display()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")