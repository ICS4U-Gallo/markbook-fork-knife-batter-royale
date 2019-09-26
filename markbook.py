"""
Markbook Application
Group members: Aidan, Ryan, Henson, Eric 
"""
import pickle
import operator

all_courses = {}
all_students = {}


class course:
    def __init__(self, name, code, period, teacher):
        self.name = name
        self.code = code
        self.period = period
        self.teacher = teacher
        self.students_list = []
        self.assignment_list = []

    def add_student(self, new_student):
        if isinstance(new_student, student):
            if new_student.stu_num not in self.students_list:
                self.students_list.append(new_student.stu_num)
                new_student.course_list.append(self.code)

    def remove_student(self, stu):
        if isinstance(stu, student):
            if stu.stu_num in self.students_list:
                self.students_list.remove(stu.stu_num)
                stu.course_list.remove(self.code)

    def edit_assignement(self, ass_name):
        for assignment in self.assignment_list:
            if assignment.name == ass_name:
                while True:
                    input_ = input()
                    if input_ == "":
                        break
                    elif input_ == "a":
                        assignment.mark_stu()
                    elif input_ == "b":
                        assignment.print_mark()
                    elif input_ == "c":
                        print(assignment.average_mark())

    def add_assignment(self):
        ass_name = input("name: ")
        ass_due = input("due: ")
        ass_point = int(input("point: "))
        self.assignment_list.append(assignment(ass_name, ass_due, ass_point, self.code))

    def class_average(self):
        total = 0
        for stu in self.students_list:
            total += all_students[stu].get_average(self.code)
        average = total/len(self.students_list)
        return average


class student:
    def __init__(self, first_name, last_name, stu_num):
        self.first = first_name
        self.last = last_name
        self.stu_num = stu_num
        self.course_list = []

    def add_course(self, new_course):
        if new_course.code not in self.course_list:
            self.course_list.append(new_course.code)
            new_course.students_list.append(self.stu_num)

    def get_average(self, code):
        mark = 0
        point = 0
        cou = all_courses[code]
        for ass in cou.assignment_list:
            mark += ass.marks[self.stu_num]
            point += ass.point
        average = mark/point
        return average


class assignment:
    def __init__(self, name, due, point, course):
        self.name = name.capitalize()
        self.due = due
        self.point = point
        self.course = course
        self.marks = {}

    def mark_stu(self):
        stu = all_students[(int(input("student number: ")))]
        cou = all_courses[self.course]
        if stu.stu_num in cou.students_list:
            marks = int(input("marks: "))
            self.marks[stu.stu_num] = marks

    def print_mark(self):
        for num in self.marks:
            stu = all_students[num]
            print(stu.first, stu.last, stu.stu_num, self.marks[num])

    def average_mark(self):
        total = 0
        for mark in self.marks.values():
            total += mark
        average = ((total/len(self.marks))/self.point)*100
        return average


def course_menu():
    while True:
        print("Input nothing to go back\nInput 'a' to create a new course\nInput 'b' to edit existing courses\n"
              "Input 'c' to print all courses\nInput 'd' to print a course in detail")
        input_ = input()
        if input_ == "":
            break
        elif input_ == "a":
            create_course()
        elif input_ == "b":
            edit_course(all_courses[(input("code: ").upper())])
        elif input_ == "c":
            print_all_course()
        elif input_ == "d":
            print_course(all_courses[(input("code: ").upper())])


def create_course():
    name = input("course name: ")
    code = input("course code: ").upper()
    period = input("period: ")
    teacher = input("teacher: ")
    if code not in all_courses.keys():
        cou = course(name, code, period, teacher)
        all_courses[code] = cou


def edit_course(cou):
    while True:
        print("Input nothing to go back\nInput 'a' to add assignment \nInput 'b' to add student \n"
                  "Input 'c' to remove student \nInput 'd' to edit assignment")
        input_ = input()
        if input_ == "":
            break
        elif input_ == "a":
            cou.add_assignment()
        elif input_ == "b":
            cou.add_student(all_students[(int(input("student_num: ")))])
        elif input_ == "c":
            cou.remove_student(all_students[(int(input("student_num: ")))])
        elif input_ == "d":
            cou.edit_assignement(input("assignment name: ").capitalize())


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
            remove_student(int(input("student number: ")))
        elif input_ == "c":
            print_all_student()
        elif input_ == "d":
            print_student(all_students[(int(input("student number: ")))])
        elif input_ == "e":
            edit_student(all_students[(int(input("student number: ")))])


def edit_student(stu):
    while True:
        print("Input nothing to go back \nInput 'a' to add course")
        input_ = input()
        if input_ == "":
            break
        elif input_ == "a":
            stu.add_course(all_courses[(input("code: ").upper())])


def create_student():
    print("Creating new student")
    first_name = input("first name: ")
    last_name = input("last name: ")
    stu_num = int(input("student number: "))
    if stu_num not in all_students.keys():
        new_student = student(first_name, last_name, stu_num)
        all_students[stu_num] = new_student


def remove_student(stu):
    del all_students[stu]


def print_all_student():
    for stu in all_students.values():
        print(stu.first, stu.last, stu.stu_num)


def print_student(stu):
    print(stu.first, stu.last, stu.stu_num)
    for code in stu.course_list:
        cou = all_courses[code]
        print(cou.name, stu.get_average(cou.code))


def print_all_course():
    for cou in all_courses.values():
        print(cou.name, cou.code, len(cou.students_list))


def print_course(course):
    print(course.name, course.code, course.period, course.teacher, course.class_average())
    for num in course.students_list:
        stu = all_students[num]
        print(stu.first, stu.last, stu.stu_num, stu.get_average(course.code))


def main():
    global all_students, all_courses
    with open("markbooksave", "rb") as input_:
                all_students = pickle.load(input_)
                all_courses = pickle.load(input_)
    while True:
        print("Input 'a' to manage students\nInput 'b' to manage courses\n"
              "Input 's' to save")
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

'''
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
'''