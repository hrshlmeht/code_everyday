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
# ss = 'Harshal$$$$$Mehta'
# ss1 = ss.capitalize()
# print (ss1)
#
#
# ss2 = ss.encode()
#
# print (ss2)
#
#
# text = "Meet"
# x = text.center(20, 'x' )
# print (x)



# class meet:
#     def __init__(self , name , age ) :
#         self.name = name
#         self.age = age
#         print(f"We have added {name} who is aging {age}" )
#
#     def update(self , name , new_age ):
#         self.age = new_age
#         print(f"The updated age of {name}  is {new_age}")
#
#     # def delete(self, deleted_name ):
#     #     self.name = deleted_name
# class delete(meet):
#     def delete_wala(self ,delete_data  ):
#         self.delete = delete_data
#         print(f"The person having  data has been deleted as per {delete_data}")


# print("Please enter  your name and age")
# input_name = input()
# input_age = input()
# s = meet(input_name , input_age)
# print("Please enter the age you want to update")
# input_newage = input()
# s.update( input_name , input_newage )
# print("Enter the name you want to delete ")
# delete_name = input()
# d  = delete(input_name , input_age)
# d.delete_wala(delete_name)




# existing_user = ['Harshal', 'Meet', 'Harshank', 'Golo', 'Keval']
#
# class library:
#
#     def library_create(self , user_name):
#         self.name = user_name
#         if user_name  in existing_user:
#           print('The user is already existing please proceed to purchase the book')
#         else :
#           print('The user is not present please register the user first')
#
#     def library_update(self, user_name):
#         self.name =user_name
#         if user_name in existing_user:
#             existing_user.remove(user_name)
#             print( f'The user has been deleted and the updated list is {existing_user}')
#



# lib = library()
# print('Enter the name of the user')
# name = input()
# lib.library_create(name)
# print('Enter the name of the user to delete the record ')
# name_update = input()
# lib.library_update(name_update)



# l= [10 , 11 ,12 , 13 , 14]
#
# class main:
#     def imp_func(self):
#         for i in range(len(l)):
#             print(f"The {i} element is {l[i]}")
#
#     def altering(self , index , modified):
#         l[index] = modified
#         print(l)
#
#     def add_person(self):
#         print("Enter the name of the person to append list")
#         person = input()
#         l.append(person)
#         print(f"The new updated list is {l}")
#
#
# m = main()
# m.imp_func()
# print('Enter the index to modify')
# index_from_user = int(input())
# modified_data=input()
# m.altering(index_from_user , modified_data )
# m.add_person()


#leetcode problem of longest prefix
# strs = ['flower' , 'flow ', 'flowing ']
#
# def solution():
#     result = " "
#     for s in range(len(strs[0])):
#         for i in strs:
#             if i == len(s) or s[i]!= strs[0][1]:
#                 print (result)
#         result += strs[0][i]
#
#     print (result)
#
import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def main (stdscr):
    stdscr.clear()
    stdscr.addstr(0 , 0 , "Hello World")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)




