from database import load_students, save_students

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    students = load_students()

    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        branch = input("Enter Branch: ")

        student = {
            "roll": roll,
            "name": name,
            "age": age,
            "branch": branch
        }

        students.append(student)
        save_students(students)
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for s in students:
                print("----------------------")
                print("Roll   :", s["roll"])
                print("Name   :", s["name"])
                print("Age    :", s["age"])
                print("Branch :", s["branch"])

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
