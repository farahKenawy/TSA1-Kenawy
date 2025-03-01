# Open the file in read mode
try:
    with open("students.txt", "r") as file:
        # Reading the file content
        student_data = file.read()

        # Displaying student information
        print("Reading Student Information:\n")
        print(student_data)

except FileNotFoundError:
    print("Error: 'students.txt' not found. Please add student information first.")
