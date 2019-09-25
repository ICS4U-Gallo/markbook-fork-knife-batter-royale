"""
Markbook Application
Group members: Aidan, Ryan, Henson, Eric 
"""
import pickle

all_courses = []
all_students = []


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
        pass

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
        cou = find_course(code)
        for ass in cou.assignment_list:
            mark = ass.marks(self.stu_num)
            point = ass.points
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
        stu = find_student(int(input("student number: ")))
        cou = find_course(self.course)
        if stu.stu_num in cou.students_list:
            marks = int(input("marks: "))
            self.marks[stu.stu_num] = marks

    def print_mark(self):
        for stud in self.marks:
            stu = find_student(stud)
            print(stu.first, stu.last, stu.stu_num, self.marks[stud])

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
            edit_course(find_course(input("code: ").upper()))
        elif input_ == "c":
            print_all_course()
        elif input_ == "d":
            print_course(find_course(input("code: ").upper()))


def create_course():
    name = input("course name: ")
    code = input("course code: ").upper()
    period = input("period: ")
    teacher = input("teacher: ")
    cou = course(name, code, period, teacher)
    all_courses.append(cou)


def find_course(code):
    for cou in all_courses:
        if cou.code == code:
            return cou


def edit_course(cou):
    if cou in all_courses:
        while True:
            print("Input nothing to go back\nInput 'a' to add assignment \nInput 'b' to add student \n"
                "Input 'c' to remove student \nInput 'd' to edit assignment")
            input_ = input()
            if input_ == "":
                break
            elif input_ == "a":
                cou.add_assignment()
            elif input_ == "b":
                cou.add_student(find_student(int(input("student_num: "))))
            elif input_ == "c":
                cou.remove_student(find_student(int(input("student_num: "))))
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
    all_students.remove(stu)
    del stu


def print_all_student():
    for stu in all_students:
        print(stu.first, stu.last, stu.stu_num)


def print_student(stu):    
    print(stu.first, stu.last, stu.stu_num)
    for course in stu.course_list:
        cou = find_course(course)
        print(cou.name)


def print_all_course():
    for cou in all_courses:
        print(cou.name, cou.code, len(cou.students_list))


def print_course(course):
    print(course.name, course.code, course.period, course.teacher)
    for stud in course.students_list:
        stu = find_student(stud)
        print(stu.first, stu.last, stu.stu_num)


def print_menu():
    print("Input 'a' to manage students\nInput 'b' to manage courses\n"
          "Input 's' to save and exit")


def main():
    global all_students, all_courses
    with open("markbooksave", "rb") as input_:
                all_students = pickle.load(input_)
                all_courses = pickle.load(input_)
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
            break


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
