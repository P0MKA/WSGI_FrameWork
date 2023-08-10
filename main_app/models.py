from copy import deepcopy

from main_app.middleware import Subject

class User:
    count = 0
    def __init__(self, username, email, phone):
        self.id = User.count
        User.count =+ 1
        self.username = username
        self.email = email
        self.phone = phone


class Course(Subject):
    def __init__(self, name, category, **kwargs):
        super().__init__()
        self.name = name
        self.students = []
        self.category = category
        self.category.courses.append(self)

    def __iter__(self):
        for student in self.students:
            return student


    def clone(self):
        course = deepcopy(self)
        course.name = f"{self.name}_copy"
        course.category = self.category
        self.category.courses.append(course)
        course.students.clear()
        return course

    def add_studdents(self, student):
        self.students.append(student)
        self.notify
class OfflineCourse(Course):
    def __init__(self, name, category, place=None, **kwargs):
        super().__init__(name, category)
        self.place = place


class OnlineCourse(Course):
    def __init__(self, name, category, platform=None, **kwargs):
        super().__init__(name, category)
        self.platform = platform


class CourseFactory:
    courses = {
        "offline": OfflineCourse,
        "online": OnlineCourse,
    }

    @classmethod
    def create(cls, course_type, name, category, **kwargs):
        return cls.courses[course_type](name, category, **kwargs)


class Category:
    id_counter = 0

    def __init__(self, name):
        self.id = Category.id_counter
        Category.id_counter += 1
        self.name = name
        self.courses = []

    def __iter__(self):
        for course in self.courses:
            yield course

    def __repr__(self):
        return f"Category {self.name}"

    def course_count(self):
        return len(self.courses)