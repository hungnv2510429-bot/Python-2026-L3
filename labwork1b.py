# ==========================================
# PRACTICAL WORK 1: STUDENT MARK MANAGEMENT
# ==========================================

# -----------------------------
# INPUT FUNCTIONS
# -----------------------------

def input_students():
    students = {}

    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\n--- Student {i + 1} ---")

        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter date of birth (DD/MM/YYYY): ")

        students[student_id] = {
            "name": name,
            "dob": dob
        }

    return students


def input_courses():
    courses = {}

    n = int(input("\nEnter number of courses: "))

    for i in range(n):
        print(f"\n--- Course {i + 1} ---")

        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")

        courses[course_id] = course_name

    return courses


def input_marks(students, courses, marks):
    if len(students) == 0:
        print("\nThere are no students.")
        return

    if len(courses) == 0:
        print("\nThere are no courses.")
        return

    print("\n========== COURSE LIST ==========")

    for course_id, course_name in courses.items():
        print(f"{course_id} - {course_name}")

    course_id = input("\nSelect course ID: ")

    # Check whether course exists
    if course_id not in courses:
        print("Course does not exist!")
        return

    # Create dictionary for this course
    if course_id not in marks:
        marks[course_id] = {}

    print(f"\nEnter marks for course: {courses[course_id]}")

    for student_id, student_info in students.items():

        while True:
            try:
                mark = float(
                    input(
                        f"Enter mark for "
                        f"{student_id} - {student_info['name']}: "
                    )
                )

                if 0 <= mark <= 10:
                    break
                else:
                    print("Mark must be between 0 and 10.")

            except ValueError:
                print("Please enter a valid number.")

        marks[course_id][student_id] = mark

    print("\nMarks entered successfully!")


# -----------------------------
# LISTING FUNCTIONS
# -----------------------------

def list_courses(courses):
    print("\n========== COURSES ==========")

    if len(courses) == 0:
        print("No courses.")
        return

    for course_id, course_name in courses.items():
        print(f"ID: {course_id} | Name: {course_name}")


def list_students(students):
    print("\n========== STUDENTS ==========")

    if len(students) == 0:
        print("No students.")
        return

    for student_id, student_info in students.items():
        print(
            f"ID: {student_id} | "
            f"Name: {student_info['name']} | "
            f"DoB: {student_info['dob']}"
        )


def show_student_marks(students, courses, marks):
    print("\n========== SHOW STUDENT MARKS ==========")

    if len(courses) == 0:
        print("No courses.")
        return

    print("\nAvailable courses:")

    for course_id, course_name in courses.items():
        print(f"{course_id} - {course_name}")

    course_id = input("\nEnter course ID: ")

    if course_id not in courses:
        print("Course does not exist!")
        return

    print(f"\nCourse: {courses[course_id]}")
    print("------------------------------------------")

    if course_id not in marks:
        print("No marks have been entered for this course.")
        return

    for student_id, mark in marks[course_id].items():

        student_name = students[student_id]["name"]

        print(
            f"Student ID: {student_id} | "
            f"Name: {student_name} | "
            f"Mark: {mark:.2f}"
        )


# -----------------------------
# MAIN PROGRAM
# -----------------------------

def main():

    # Data
    students = {}
    courses = {}
    marks = {}

    while True:

        print("\n")
        print("==========================================")
        print("       STUDENT MARK MANAGEMENT")
        print("==========================================")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a course")
        print("0. Exit")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            students = input_students()

        elif choice == "2":
            courses = input_courses()

        elif choice == "3":
            input_marks(students, courses, marks)

        elif choice == "4":
            list_students(students)

        elif choice == "5":
            list_courses(courses)

        elif choice == "6":
            show_student_marks(students, courses, marks)

        elif choice == "0":
            print("\nProgram ended.")
            break

        else:
            print("\nInvalid choice! Please try again.")


# Run program
if __name__ == "__main__":
    main()