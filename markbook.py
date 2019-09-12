"""
Markbook Application
Group members: 
"""


class course:
    def __init__(self, name, code, period, teacher, students):
        self.name = name
        self.code = code
        self.period = period
        self.teacher = teacher
        self.students_list = students

    def add_student(self, new_student):
        self.students_list.append(new_student)


class student:
    def __init__(self, first_name, last_name, age, gender, stu_num, email):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.gender = gender
        self.stu_num = stu_num
        self.email = email


all_students = [student("a", "a", "a", "a", "a", "a"), 
                student("b", "b", "b", "b", "b", "b"), 
                student(c, c, c, c, c, c), student(d, d, d, d, d, d),
                student(e, e, e, e, e, e), student(f, f, f, f, f, f),
                student(g, g, g, g, g, g), student(h, h, h, h, h, h),
                ]


def create_student():
    print("Creating new student")
    first_name = input("first name: ")
    last_name = input("last name: ")
    age = input("age: ")
    gender = input("gender: ")
    stu_num = input("student number: ")
    email = input("email: ")
    new_student = student(first_name, last_name, age, gender, stu_num, email)
    all_students.append(new_student)


def print_all_student():
    for stu in all_students:
        print(stu.first, stu.last, stu.stu_num)


def main():
    while True:
        inp = input()
        if inp == "": 
            create_student()
        elif inp == " ":
            print_all_student()


if __name__ == "__main__":
    main()