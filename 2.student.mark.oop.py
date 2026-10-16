import math
import numpy as np
import curses


# =========================
# COURSE CLASS
# =========================

class Course:
    def __init__(self, name, credit, mark):
        self.name = name
        self.credit = credit
        self.mark = mark

    def round_mark(self):
        # Round DOWN to 1 decimal place
        self.mark = math.floor(self.mark * 10) / 10

    def __str__(self):
        return f"{self.name} - {self.credit} credits - {self.mark}"


# =========================
# STUDENT CLASS
# =========================

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def calculate_gpa(self):
        if len(self.courses) == 0:
            return 0

        credits = np.array([course.credit for course in self.courses])
        marks = np.array([course.mark for course in self.courses])

        weighted_sum = np.sum(credits * marks)
        total_credits = np.sum(credits)

        if total_credits == 0:
            return 0

        gpa = weighted_sum / total_credits

        # Round DOWN to 1 decimal place
        gpa = math.floor(gpa * 10) / 10

        return gpa

    def round_all_marks(self):
        for course in self.courses:
            course.round_mark()

    def __str__(self):
        return f"{self.student_id} - {self.name} - GPA: {self.calculate_gpa()}"


# =========================
# CREATE STUDENTS
# =========================

def create_students():
    students = []

    s1 = Student("SV001", "Nguyen Van An")
    s1.add_course(Course("Python", 3, 8.76))
    s1.add_course(Course("Math", 3, 7.83))
    s1.add_course(Course("Database", 2, 9.15))

    s2 = Student("SV002", "Tran Van Binh")
    s2.add_course(Course("Python", 3, 9.25))
    s2.add_course(Course("Math", 3, 8.42))
    s2.add_course(Course("Database", 2, 7.95))

    s3 = Student("SV003", "Le Van Cuong")
    s3.add_course(Course("Python", 3, 6.84))
    s3.add_course(Course("Math", 3, 7.26))
    s3.add_course(Course("Database", 2, 8.11))

    students.append(s1)
    students.append(s2)
    students.append(s3)

    return students


# =========================
# SORT STUDENTS
# =========================

def sort_students_by_gpa(students):
    students.sort(
        key=lambda student: student.calculate_gpa(),
        reverse=True
    )


# =========================
# CURSES UI
# =========================

def curses_ui(stdscr, students):

    try:
        curses.curs_set(0)
    except:
        pass

    stdscr.clear()

    height, width = stdscr.getmaxyx()

    title = "STUDENT MANAGEMENT SYSTEM"

    stdscr.addstr(
        1,
        max(0, (width - len(title)) // 2),
        title,
        curses.A_BOLD
    )

    stdscr.addstr(3, 2, "Student ID")
    stdscr.addstr(3, 20, "Name")
    stdscr.addstr(3, 45, "GPA")

    stdscr.addstr(4, 2, "-" * 60)

    row = 5

    for student in students:

        if row >= height - 2:
            break

        stdscr.addstr(row, 2, student.student_id)
        stdscr.addstr(row, 20, student.name)
        stdscr.addstr(row, 45, f"{student.calculate_gpa():.1f}")

        row += 1

    stdscr.addstr(
        height - 2,
        2,
        "Press any key to exit..."
    )

    stdscr.refresh()
    stdscr.getch()


# =========================
# MAIN
# =========================

def main():

    students = create_students()

    # Round down all course marks
    for student in students:
        student.round_all_marks()

    # Sort by GPA descending
    sort_students_by_gpa(students)

    # Display using curses
    curses.wrapper(curses_ui, students)


if __name__ == "__main__":
    main()
    