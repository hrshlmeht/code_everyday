# class Person:
#   def __init__(self, name=None, age=None):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"Name:{self.name} Age:({self.age})"
#
# p1 = Person(age=36)
#
# print(p1.name)
# print(p1)
#


# class Dog:
#
#   def __init__(self, name ):
#      self.function_attribute  = name
#      print(name)
#
#   def  add_one (self , x ):
#        print  (x + 1)
#
#   def yolo (self):
#       print ("Munni badnam")
#
# print("Enter the name of the dog")
# name = input()
# d = Dog(name)
# d.add_one(5)
# d.yolo()


class Student:
    def __init__(self, name , age , grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self ,course_name , max_students):
        self.name = course_name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False


    def average(self):
        count = 0
        for student in self.students:
            count += student.get_grade()

        return count/len(self.students)

s1 = Student("Yolo " , 40 , 80)
s2 = Student("Polo" , 42 , 70)
s3 = Student('Golo' , 44, 67)

course = Course("SEPM", 6)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.average())









