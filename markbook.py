"""
Markbook Application
Group members:
"""
import pickle


class course:
    def __init__(self, name, code, period, teacher):
        self.name = name
        self.code = code
        self.period = period
        self.teacher = teacher
        self.students_list = []
        self.assignment_list = []

    def add_student(self, new_student):
        self.students_list.append(new_student)
        new_student.add_course(self)

    def add_assignment(self):
        ass_name = input("name: ")
        ass_due = input("due: ")
        ass_point = input("point: ")
        self.assignment_list.append(assignment(ass_name, ass_due, ass_point))


class student:
    def __init__(self, first_name, last_name, stu_num):
        self.first = first_name
        self.last = last_name
        self.stu_num = stu_num
        self.course_list = []

    def add_course(self, new_course):
        self.course_list.append(new_course)
        new_course.students_list.append(self)


class assignment:
    def __init__(self, name, due, point):
        self.name = name
        self.due = due
        self.point = point


def course_menu():
    while True:
        print("Input nothing to go back\nInput 'a' to create a new course\nInput 'b' to edit existing courses\n"
              "Input 'c' to print all courses\nInput 'd' to print a course in detail")
        input_ = input()
        if input_ == "":
            break
        elif input_ == "a":
            pass
        elif input_ == "b":
            edit_course(find_course(input("code: ").upper()))
        elif input_ == "c":
            print_all_course()
        elif input_ == "d":
            print_course(find_course(input("code: ").upper()))


def find_course(code):
    for course in all_courses:
        if course.code == code:
            return course


def edit_course(course):
    while True:
        print("Input nothing to go back\nInput 'a' to add assignment")
        input_ = input()
        if input_ == "":
            break
        elif input_ == "a":
            course.add_assignment()


def student_menu():
    while True:
        print("Input nothing to go back\nInput 'a' to add a student\nInput 'b' to remove students\nInput 'c' to show the student list\n"
              "Input 'd' to show a student detail\nInput 'e' to edit a student")
        input_ = input()
        if input_ == "":
            break
        elif input_ == "a":
            create_student()
        elif input_ == "b":
            remove_student(find_student(int(input("student number: "))))
        elif input_ == "c":
            print_all_student()
        elif input_ == "d":
            print_student(find_student(int(input("student number: "))))
        elif input_ == "e":
            edit_student(find_student(int(input("student number: "))))


def find_student(num):
    for stu in all_students:
        if stu.stu_num == num:
            return stu


def edit_student(stu):
    while True:
        print("Input nothing to go back \nInput 'a' to add course")
        input_ = input()
        if input_ == "":
            break
        elif input_ == "a":
            stu.add_course(find_course(input("code: ").upper()))


def create_student():
    print("Creating new student")
    first_name = input("first name: ")
    last_name = input("last name: ")
    stu_num = int(input("student number: "))
    new_student = student(first_name, last_name, stu_num)
    all_students.append(new_student)


def remove_student(stu):
    del stu


def print_all_student():
    for stu in all_students:
        print(stu.first, stu.last, stu.stu_num)


def print_student(stu):    
    print(stu.first, stu.last, stu.stu_num)
    for course in stu.course_list:
        print(course.name)


def print_all_course():
    for cou in all_courses:
        print(cou.name, cou.code, len(cou.students_list))


def print_course(course):
    print(course.name, course.code, course.period, course.teacher)
    for stu in course.students_list:
        print(stu.first, stu.last, stu.stu_num)


def print_menu():
    print("Input 'a' to manage students\nInput 'b' to manage courses\nInput 's'"
          "to save changes")

all_students = [student("a", "a", 1),
                student("b", "b", 2),
                student("c", "c", 3),
                student("d", "d", 4),
                student("e", "e", 5),
                student("f", "f", 6),
                student("g", "g", 7),
                student("h", "h", 8),
                ]
all_courses = [course("comp sci", "ICS4U", 2, "Gallo")]


def main():
    global all_students, all_courses
    """
    with open("markbooksave", "rb") as input_:
                all_students = pickle.load(input_)
                all_courses = pickle.load(input_)
    """
    while True:
        print_menu()
        input_ = input()
        if input_ == "a":
            student_menu()
        elif input_ == "b":
            course_menu()
        elif input_ == "s":
            with open("markbooksave", "wb") as output:
                pickle.dump(all_students, output, pickle.HIGHEST_PROTOCOL)
                pickle.dump(all_courses, output, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()

from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    return {}


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    return {}


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    return 0


def add_student_to_classroom(student, classroom):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    pass


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    pass


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    pass
