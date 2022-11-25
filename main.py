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


# class Student:
#     def __init__(self, name , age , grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def get_grade(self):
#         return self.grade
#
#
# class Course:
#     def __init__(self ,course_name , max_students):
#         self.name = course_name
#         self.max_students = max_students
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#
#     def average(self):
#         count = 0
#         for student in self.students:
#             count += student.get_grade()
#
#         return count/len(self.students)
#
# s1 = Student("Yolo " , 40 , 80)
# s2 = Student("Polo" , 42 , 70)
# s3 = Student('Golo' , 44, 67)
#
# course = Course("SEPM", 6)
# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)
# print(course.average())

#learning inhertitance
# class animal:
#     def __init__(self, name , age ):
#         self.name = name
#         self.age = age
#
#     def speak_func(self):
#         print("This is the function in parent class")
#
#
# class cat(animal):
#     def __init__(self, name , age , colour):
#         super().__init__(name, age)
#         self.colour = colour
#
#     def show_func(self):
#         print (f"I am {self.name} my age is {self.age} and my color is {self.age}")
#
#
#     def speak_func(self):
#         print("Meow meow ")
#
#
#
# class dog(animal):
#     def speak_func(self):
#         print("Bhow Bhow ")
#
# a = animal('Yolo', 25)
# a.speak_func()
# d = dog('Polo', 36)
# c = cat("Billi",3,"Black")
# c.show_func()
# d.speak_func()

#global variable concept

# class Person:
#     number_of_people = 0
#
#     def __init__(self , age , name ):
#         self.age = age
#         self.name = name
#
# p1 = Person('Harsha', 4)
# p2 = Person('Keval', 4)
# Person.number_of_people = 8
# print(p2.number_of_people)
# print(p1.number_of_people)


#capitalize method
ss = 'Harshal$$$$$Mehta'
ss1 = ss.capitalize()
print (ss1)


ss2 = ss.encode()

print (ss2)