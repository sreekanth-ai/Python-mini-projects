students = []

def add_student():
    name = input("enter student name : ")
    roll = input("enter the roll no : ")
    marks = int(input("enter the marks : "))

    student = {
        'name' : name,
        'roll' : roll,
        'marks' : marks
    }
    students.append(student)

def view_student():
    if not students:
        print("No student found")
        return
    for student in students:
        print(student)

def check_results():
    name = input("Enter name : ")
    for student in students:
        if student['name'] == name:
            print(f"{name} marks is : ", student['marks'])
            return 
    print("No student found")

while True : 
    print("\n 1.Add Student")
    print("2.View Student")
    print("3.Check Results")
    print("4.Exit")

    choice = input("Enter choice : ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        check_results()
    elif choice == "4":
        break
    else:
        print(" Invalid Choice")