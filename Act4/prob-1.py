import json
from operator import itemgetter

# Define the file name
FILENAME = "students.json"

# Sample student records (StudentID, (FirstName, LastName), ClassStanding, MajorExam)
students = [
    (100001, ("John", "Doe"), 85, 90),
    (100002, ("Jane", "Smith"), 78, 88),
    (100003, ("Alice", "Johnson"), 92, 85),
]

def save_file():
    with open(FILENAME, "w") as file:
        json.dump(students, file)
    print("Records saved successfully!")

def load_file():
    global students
    try:
        with open(FILENAME, "r") as file:
            students = json.load(file)
        print("Records loaded successfully!")
    except FileNotFoundError:
        print("No existing file found.")

def save_as_file(new_filename):
    with open(new_filename, "w") as file:
        json.dump(students, file)
    print(f"Records saved as {new_filename}!")

def show_all_students():
    for student in students:
        print(student)

def order_by_last_name():
    sorted_students = sorted(students, key=lambda s: s[1][1])
    for student in sorted_students:
        print(student)

def order_by_grade():
    sorted_students = sorted(students, key=lambda s: s[2] * 0.6 + s[3] * 0.4, reverse=True)
    for student in sorted_students:
        print(student)

def show_student_record(student_id):
    for student in students:
        if student[0] == student_id:
            print(student)
            return
    print("Student not found!")

def add_record():
    student_id = int(input("Enter Student ID (6-digit): "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    students.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Student added successfully!")

def edit_record(student_id):
    for i, student in enumerate(students):
        if student[0] == student_id:
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing Grade: "))
            major_exam = float(input("Enter New Major Exam Grade: "))
            students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Student record updated successfully!")
            return
    print("Student not found!")

def delete_record(student_id):
    global students
    students = [s for s in students if s[0] != student_id]
    print("Student record deleted!")

def main():
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            load_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            filename = input("Enter new filename: ")
            save_as_file(filename)
        elif choice == "4":
            show_all_students()
        elif choice == "5":
            order_by_last_name()
        elif choice == "6":
            order_by_grade()
        elif choice == "7":
            student_id = int(input("Enter Student ID: "))
            show_student_record(student_id)
        elif choice == "8":
            add_record()
        elif choice == "9":
            student_id = int(input("Enter Student ID to edit: "))
            edit_record(student_id)
        elif choice == "10":
            student_id = int(input("Enter Student ID to delete: "))
            delete_record(student_id)
        elif choice == "11":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
