class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = 0

    def grades_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_course:
                lecturer.grades_course[course] += [grade]
            else:
                lecturer.grades_course[course] = [grade]
        else:
            return
        count = 0
        len_ = 0
        for key in lecturer.grades_course.keys():
            for grade in list(lecturer.grades_course[key]):
                count = count + grade
                len_ += 1
        lecturer.average_grades = round(count / len_, 2)

    def __str__(self):
        text = f"""
        Имя: {self.name} 
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.grades}
        Курсы в процессе изучения: {self.courses_in_progress}
        Завершенные курсы: {self.finished_courses}"""
        return text

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grades < other.average_grades
        else:
            return 'Нельзя сравнить'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_course = {}
        self.average_grades = 0

    def __str__(self):
        text = f"""
        Имя: {self.name} 
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.average_grades}"""
        return text

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grades < other.average_grades
        else:
            return 'Нельзя сравнить'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        count = 0
        len_ = 0
        for key in student.grades.keys():
            for grade in list(student.grades[key]):
                count = count + grade
                len_ += 1
        student.average_grades = round(count / len_, 2)

    def __str__(self):
        text = f"""
        Имя: {self.name}
        Фамилия: {self.surname}"""
        return text


student_1 = Student('Ruoy', 'Eman', 'man')
student_1.courses_in_progress += ['Python']
# print(student_1)
student_2 = Student('Bob', 'Marly', 'man')
student_2.courses_in_progress += ['Python']
# print(student_2)
lect_1 = Lecturer('Bob', 'Frost')
lect_1.courses_attached = 'Python'
lect_2 = Lecturer('Ilon', 'Mask')
lect_2.courses_attached = 'Python'

# student_1.grades_lecturer(lect_1, 'Python', 8)
# student_2.grades_lecturer(lect_1, 'Python', 10)
# student_1.grades_lecturer(lect_2, 'Python', 9)
# student_2.grades_lecturer(lect_2, 'Python', 10)

review_1 = Reviewer('Fill', 'Smitch')
review_1.courses_attached = 'Python'
# review_1.rate_hw(student_1, 'Python', 10)
# review_1.rate_hw(student_1, 'Python', 10)
#
# review_1.rate_hw(student_2, 'Python', 10)
# review_1.rate_hw(student_2, 'Python', 8)
# print(lect_1)
# print(student_1.average_grades)
# print(student_2.average_grades)
# print(lect_1.average_grades)
# print(lect_2.average_grades)
# print(lect_1 < lect_2)
# print(student_1 < (student_2))

# DZ№4

student_list = [student_1, student_2]
lecturer_list = [lect_1, lect_2]
student_1.grades_lecturer(lect_1, 'Python', 10)
student_1.grades_lecturer(lect_2, 'Python', 10)
student_2.grades_lecturer(lect_1, 'Python', 9)
student_2.grades_lecturer(lect_2, 'Python', 10)
print(f'Средняя оценка за дз {student_1.surname} больше {student_2.surname}: {student_1.average_grades < student_2.average_grades}')
review_1.rate_hw(student_1, 'Python', 9)
review_1.rate_hw(student_1, 'Python', 8)
review_1.rate_hw(student_2, 'Python', 10)
review_1.rate_hw(student_2, 'Python', 10)
print(f'Средняя оценка за лекциии {lect_1.surname} больше {lect_2.surname}: {lect_1.average_grades < lect_2.average_grades}')

# print(student_2.average_grades)
# print(lect_2.grades_course)
# print(student_2.grades)
print(student_1)
print(student_2)
print(lect_1)
print(lect_2)
print(review_1)

def average_lecturer(lecturers, courses):
    count_grades = 0
    aver = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades_course.items():
            if courses in key:
                count_grades += sum(value) / len(value)
                aver += 1
    return round(count_grades / aver, 2)

def average_student(students, courses):
    count_grades = 0
    aver = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                count_grades += sum(value) / len(value)
                aver += 1
    return round(count_grades / aver, 2)

print(f'Средняя оценка лекторов за курс "Python": {average_lecturer(lecturer_list, "Python")}')
print(f'Средняя оценка студентов за курс "Python": {average_student(student_list, "Python")}')
