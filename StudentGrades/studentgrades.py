student_grade = {}
def add_student(name , grade):
    student_grade[name] = grade
    print(f"Added {name} with a {grade}")
def update(name , grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found")
def delete(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} with marks are updated")
def display():
    if student_grade:
        for name , grade in student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("No students found/added")
def main():
    while True:
        print("\n Student Grades Management system")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View student")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter stuent name: ")
            grade = int(input("Enter student's grade: "))
            add_student(name,grade)
        elif choice == 2:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            update(name , grade)
        elif choice == 3:
            name = input("Enter student name")
            delete(name)
        elif choice == 4:
            display()
        elif choice == 5:
            print("Closing the program")
            break
            
        else:
            print("Invalid choice")
main()
