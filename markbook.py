"""
Markbook Application
Group members:
"""
import pickle


class course:
    def __init__(self, name, code, period, teacher, students):
        self.name = name
        self.code = code
        self.period = period
        self.teacher = teacher
        self.students_list = students
        self.assignment = []

    def add_student(self, new_student):
        self.students_list.append(new_student)

    def add_assignment(self):
        ass_name = input("name: ")
        ass_due = input("due: ")
        ass_point = input("point: ")
        self.assignment.append(assignment(ass_name, ass_due, ass_point))


class student:
    def __init__(self, first_name, last_name, age, gender, stu_num, email):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.gender = gender
        self.stu_num = stu_num
        self.email = email


class assignment:
    def __init__(self, name, due, point):
        self.name = name
        self.due = due
        self.point = point


def course_menu():
    print("course")
    while True:
        input_ = input()
        if input_ == "":
            break
        elif input_ == "a":
            edit_course(input("code: ").upper())


def edit_course(code):
    for cou in all_courses:
        if cou.code == code:
            while True:
                input_ = input()
                if input_ == "":
                    break
                elif input_ == "a":
                    cou.add_assignment()


def student_menu():
    print("student")
    while True:
        input_ = input()
        if input_ == "":
            break
        elif input_ == "a":
            create_student()
        elif input_ == "b":
            remove_student(input("stu_num"))


def create_student():
    print("Creating new student")
    first_name = input("first name: ")
    last_name = input("last name: ")
    age = int(input("age: "))
    gender = input("gender: ")
    stu_num = int(input("student number: "))
    email = input("email: ")
    new_student = student(first_name, last_name, age, gender, stu_num, email)
    all_students.append(new_student)


def remove_student(stu_num):
    for stu in all_students:
        if stu.stu_num == stu_num:
            del stu


def print_all_student():
    for stu in all_students:
        print(stu.first, stu.last, stu.stu_num)


def print_all_course():
    for cou in all_courses:
        print(cou.name, cou.code, len(cou.students_list))


def print_course(code):
    for cou in all_courses:
        if cou.code == code:
            print(cou.name, cou.code, cou.period, cou.teacher)
            for stu in cou.students_list:
                print(stu.first, stu.last, stu.stu_num)


def print_menu():
    print("print")
    while True:
        input_ = input("")
        if input_ == "":
            break
        elif input_ == "a":
            print_all_student()
        elif input_ == "b":
            print_all_course()
        elif input_ == "c":
            print_course(input("code").upper())
    

def main():
    global all_students, all_courses
    with open("markbooksave", "rb") as input_:
                all_students = pickle.load(input_)
                all_courses = pickle.load(input_)
    while True:
        input_ = input()
        if input_ == "a":
            print_menu()
        elif input_ == "b":
            student_menu()
        elif input_ == "c":
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
