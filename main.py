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

# learning inhertitance
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

# global variable concept

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


# capitalize method
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


# leetcode problem of longest prefix
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

#####################################################################
############we cannot import curses in any IDE , however we can write trhis program in 1 file and run it using cmd. Its a group approach for running programs having curses library
# import curses
# from curses import wrapper
# import queue
# import time
# maze = [
#     ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
#     ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
#     ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
#     ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
#     ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
#     ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
#     ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
# ]
#
# def print_maze(maze, stdscr, path=[]):
#     BLUE = curses.color_pair(1)
#     RED = curses.color_pair(2)
#
#     for i, row in enumerate(maze):
#         for j, value in enumerate(row):
#             if (i, j) in path:
#                 stdscr.addstr(i, j*2, "X", RED)
#             else:
#                 stdscr.addstr(i, j*2, value, BLUE)
#
#
# def find_start(maze, start):
#     for i, row in enumerate(maze):
#         for j, value in enumerate(row):
#             if value == start:
#                 return i, j
#     return None
#
#
# def find_path(maze, stdscr):
#     start = "O"
#     end = "X"
#     start_pos = find_start(maze, start)
#     q = queue.Queue()
#
#     q.put((start_pos, [start_pos]))
#
#     visited = set()
#     while not q.empty():
#         current_pos, path = q.get()
#         row, col = current_pos
#         stdscr.clear()
#         print_maze(maze, stdscr, path)
#         time.sleep(0.2)
#         stdscr.refresh()
#
#         if maze[row][col] == end:
#             return path
#
#         neighbors = find_neighbors(maze, row, col)
#         for neighbor in neighbors:
#             if neighbor in visited:
#                 continue
#
#             r, c = neighbor
#             if maze[r][c] == "#":
#                 continue
#
#             new_path = path + [neighbor]
#
#             q.put((neighbor, new_path))
#
#             visited.add(neighbor)
#
# def find_neighbors(maze, row, col):
#     neighbors = []
#     if row > 0:  # check up
#         neighbors.append((row - 1, col))
#     if row + 1 < len(maze):  # check down
#         neighbors.append((row + 1, col))
#     if col > 0:  # check left
#         neighbors.append((row, col - 1))
#     if col + 1 < len(maze[0]):  # check right
#         neighbors.append((row, col + 1))
#     return neighbors
#
# def main(stdscr):
#     curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
#     curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
#     find_path(maze, stdscr)
#     stdscr.getch()
# wrapper(main)


# print('Enter the number for displaying the table')
# num = int(input())
#
# for i  in range( 1 , 11):
#     print( i* num)
#
# sample_list = ['Yolo' , 'Polo', 'Golo']
# hash = enumerate(sample_list)

# print (list(hash))
#
# print('Enter the number of students in the list')
# num = int(input())
# students = list()
#
# for i in range(num):
#     print("Enter the name of students")
#     student = input()
#     students.append(student)
#
# print(students)
#
# enum_stu = enumerate(students)
# print(list(enum_stu))


# Rows = int(input("Give the number of rows:"))
# Columns = int(input("Give the number of columns:"))
#
# # Initializing the matrix
# example_matrix = []
# print("Please give the entries row-wise:")
#
# # For user input
# for  i in range(Rows):  # This for loop is to arrange rows
#     r =[]
#     for k in range(Columns):  # This for loop is to arrange columns
#         r.append(int(input()))
#     example_matrix.append(r)
#
# # Printing the matrix given by user
# for i in range(Rows):
#     for k in range(Columns):
#         print(example_matrix[i][k], end=" ")
#     print()
#


###get the data from the link - https://data.nba.net/prod/v1/today.json (open API)

# from requests import get
# from pprint import PrettyPrinter
#
# BASE_URL = "https://data.nba.net"
# ALL_JSON = "/prod/v1/today.json"
# printer = PrettyPrinter()
# data = get(BASE_URL + ALL_JSON).json()
# printer.pprint(data)

# def get_links():
#     data = get(BASE_URL + ALL_JSON).json()
#     links = data['links']
#     return links

# def get_schedule():
#     rankings = get_links()['leagueSchedule']
#     print(rankings)
#     rankings_data = get(BASE_URL + rankings).json()['league']
#     printer.pprint(rankings_data)


# def get_scoreboard():
#     scoreboard = get_links()['currentScoreboard']
#     games = get(BASE_URL + scoreboard).json()['games']
#
#     for game in games:
#         home_team = game['hTeam']
#         away_team = game['vTeam']
#
#         print('__________________________________________________________________________________________________')
#         print(f"{home_team['triCode']} VS {away_team['triCode']} ")
#         if home_team['score'] == '':
#             print('The match is not now')
#         else:
#             print(f"SCORE = {home_team['score']}  -- {away_team['score']}")
#
#
# def get_stats():
#     stats = get_links()['leagueTeamStatsLeaders']
#     data = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']
#
#     for team in data:
#         name = team['name']
#         nickname = team['nickname']
#
#         ppg = team['ppg']
#         print(f" {name} -  {nickname} has scored {ppg} in game")
#
#
#
# # get_schedule()
# #get_scoreboard()
# get_stats()

# def get_links():
#     data = get(BASE_URL+ALL_JSON).json()
#     #printer.pprint(data)
#     links = data['links']
#     printer.pprint(data)

# def get_scoreboard():
#     scoreboard = get_links()['leagueSchedule']
#     printer.pprint(leagueSchedule)

import math
import os
import random
import re
import sys

# hackerrank camel case problem
#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# def camelcase(s):
#     # Write your code here
#     count = 0
#     for i in range(len(s)):
#         j = ord(s[i])
#         if (j > 97 and j < 112):
#             i = i + 1
#         elif count = count +1
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = camelcase(s)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# leetcode remove element
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         i = 0
#         for x in nums:
#             if x != val:
#                 nums[i] = x
#                 i += 1
#         return i
#
# Leetcode for parentheses checkk not working
# s = ['(())']
# class Solution:
#     def isValid(self, s: str) -> str:
#         stack = []
#         mapClosedOpen = {")": "(", "]": "[", "}": "{"}
#
#         for c in s:
#             if c in mapClosedOpen:
#                 if stack and stack[-1] == s[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)
#         if stack == None:
#             print ('True')
#         else:
#             print ('False')
# leetcdoe for parentheses working
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#
#         mapping = {
#             '(': ')',
#             '[': ']',
#             '{': '}'
#         }
#
#         for char in s:
#             if char in mapping.keys():
#                 stack.append(mapping[char])
#             elif not stack or stack[-1] != char:
#                 return False
#             else:
#                 stack.pop()
#
#         return len(stack) == 0


# names = []
# print("Enter the number of studens you want to add to the record")
# no = int(input())
# for i in range(no):
#     print("Enter the name of the student to be added ")
#     name = input()
#     names.append(name)
#     print("Record added succesfully")
#
# print("Enter the name of student you want to search ")
# name_search = input()
# if name_search in names:
#     print ("Yes it is present")
# else:
#     print ("The person is not present")
#
# print (names)
# print("Enter the name of the student you want to delete from the list")
# del_name = input()
# if del_name in names:
#     names.remove(del_name)
#     print('The updated list is ')
#     print(names)
#
#
# roll_no =  enumerate((names) , 1)
# print(list(roll_no))

# word = 'My name is Harshal Sanjay Mehta'
# for i in range(len(word)):
#     print (' '*i, word[i])

# print("Enter the number of students")
# number = int(input())
# students = []
# for i in range(number):
#     print('Enter the name of the student')
#     name = input()
#     students.append(name)
#
#
# print(students)
# print("Enter the surnames of the students")
#
# surname =[]
# print("Enter the surname of the students")
# for i in range(number):
#     sname = input()
#     surname.append(sname)
#
# print(surname)
#
# print("Merging two strings")
# i = 0
# print(students,surname)
# for i in range(number):
#     students[i]=students[i]+" "+ surname[i]
#
# print(students)


# meet = ['harhshal Mehta' ,'polo'][::-1]
# leetcdoe solution for finding the index
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         # end_num = len(nums)
#
#         # for start_num in range(end_num):
#         #     if target == nums[start_num]:
#         #         return start_num
#         #     else:
#         #         start_num = start_num + 1
#         # return start_num
#
#         if target in nums:
#             return nums.index(target)
#         else:
#             nums.append(target)
#             nums.sort()
#         return nums.index(target)


# leetcode problem for deleting duplicate emails
# sql queery for deleting duplicate emaails =
# delete
# p2
# from Person p1
#
# JOIN
# person
# p2
# ON
# p1.email = p2.email
# and p1.id < p2.id
# from pprint import PrettyPrinter
#
# BASE_URL = "https://free.currconv.com/"
# API_KEY = '7dc769f16b1b0ef349b0'
#
# printer = PrettyPrinter()
#
#
# def get_currencies():
#     endpoint = f"api/v7/currencies?apiKey={API_KEY}"
#     url = BASE_URL + endpoint
#     data = get(url).json()['results']
#     data = list(data.items())
#     data.sort()
#
#     return data
#
#
# def print_currencies(currencies):
#     for name, currency in currencies:
#         name = currency['currencyName']
#         _id = currency['id']
#
#         symbol = currency.get('currencySymbol', '')
#         print(f"{_id} - {name} - {symbol}")
#
#
# def exchange_rate(curr1 , curr2):
#     endpoint = f"api/v7/convert?q={curr1}_{curr2}&compact=ultra&apiKey={API_KEY}"
#     url = BASE_URL + endpoint
#     response = get(url)
#     data = response.json()
#
#     if len(data) == 0:
#         print('Invalid cureencies')
#         return
#
#     rate = list(data.values())[0]
#     print(f'{curr1} -> {curr2} = {data}')
#
#     return rate
#
# def convert(curr1 , curr2 , amount):
#     rate = exchange_rate(curr1 , curr2)
#     if rate is None:
#         return
#
#     try:
#         amount = float(amount)
#     except:
#         print('Invalid amount')
#         return
#
#     converted_amount = rate * amount
#     print(f'{amount} {curr1} is equal to {converted_amount}{curr2}')
#     return converted_amount
#
# # data = get_currencies()
# # print_currencies(data)
# rate=exchange_rate("CAD", "USD")
# print(rate)
#
#
# def main():
#     currencies = get_currencies()
#     print('Hello apun ne currency convert karega')
#     print('List - lists the different currencies')
#     print('Convert - convert from one currency to another')
#     print('Rate - get the exchange amount of the two currencies')
#     print()
#
#     while True:
#         command = input('Enter a command (q to quit: ').lower()
#
#         if command == 'q':
#             break
#         elif command == 'list':
#             print_currencies(currencies)
#         elif command == 'convert':
#             curr1 = input('Enter a base currency : ').upper()
#             amount = input(f"Enter an amount in {curr1} : ")
#             curr2 = input('Enter a currency to convert to :').upper()
#             convert(curr1 , curr2 , amount)
#         elif command == 'rate':
#             curr1 = input('Enter the base currency: ').upper()
#             curr2 = input('Enter a currency you want to convert to :').upper()
#             exchange_rate(curr1 , curr2)
#         else:
#             print("Unrecognized command")
#
#
#
# main()

# name = "matol"
# reverse_name = name[::-1]
# print(reverse_name)
#
# if( name == reverse_name):
#     print('this is palindrome')

array =[1,2 ,2 ,3 ,3 ,33 ,3 ,3]
print (len(array))
for i in range(len(array)):
    if array[0] == array[i]:
        print("Yes the firdt value is 1")
        if array[1] == array[i+1]:
            print('Yes the array is having second number as 2')





