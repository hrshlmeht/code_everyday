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

# array =[1,2 ,2 ,3 ,3 ,33 ,3 ,3]
# print (len(array))
# for i in range(len(array)):
#     if array[0] == array[i]:
#         print("Yes the firdt value is 1")
#         if array[1] == array[i+1]:
#             print('Yes the array is having second number as 2')

# arr = [2,2,2,2,2]
#
# arr.insert(0 , 4)
#
# print (arr)
#
# for i in arr:
#     print (' is is tatti')
#
#
# class Node:
#     def __init__(self , data=None , next = None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert_at_head(self, data):
#         node = Node(data , self.head)
#         self.head = node
#
#
#     def print(self):
#         itr = self.head
#         llstr = ' '
#         while itr:
#
#             if itr.next:
#                 suffix = '---->'
#             llstr += str(itr.data) + '--->'
#             itr = itr.next
#         print(llstr)
#
#
# if __name__ == "__main__":
#     print("Enter the number of elements to be insterted in the linked list")
#     root = LinkedList()
#     root.insert_at_head(5)
#     root.insert_at_head(12)
#     root.print()

#
# def create_phone_number():
#     print('Enter the number in the list')
#     l = int(input())
#     arr = []
#     for i in range(l):
#         print('Enter the numbers')
#         num = int(input())
#         arr.append(num)
#
#     print('(')
#     for j in range(0,3):
#         print(arr[j])
#
#     print(')')
#
#     for k in range(3 , 6):
#         print(arr[k])
#
#     print('-')
# create_phone_number()

# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np
#
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.


# int = 1234
# count = 0
# int_binary = bin(int)
# print(int_binary)
#
# for i in int_binary:
#        if i == '1':
#            print('Entering the if condition')
#            count = count + 1
#
# print(count)


# print('name harshal')
# integer = int(input())
#
# print(type(integer))

#
# def unique_in_order(iterable):
#     newList = []
#     for item in iterable:
#         if len(newList) < 1 or not item == newList[len(newList) - 1]:
#             newList.append(item)
#     print (newList)
#
# unique_in_order('AAAABBBCCDAABBB')

#leetcode solution for house robber
# class Solution(object):
#     def rob(self, nums):
#         robber_1 = 0
#         robber_2 = 0
#
#         for i in nums:
#             temp = max(robber_1 + i , robber_2)
#             # print(robber_2)
#             # print(robber_1)
#             robber_1 = robber_2
#             robber_2 = temp
#
#         return robber_2

# sorted_list = ['AAsim' , 'wakram' , 'chakram']
#
# sorted_list.sort()
# print(sorted_list)
#leetcode solution for finding length of the last word

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#
#         if (len(s) == 0):
#             return 0
#         s = s.strip() # remove the extra spaces at the end, which are unnecessary
#         l = s.split(" ") # then split it so that we get a list of all the words in the string
#         return len(l[-1])

#leetcode for solution for duplicates

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#
#         # i = len(nums)
#         # if i <= 1:
#         #     return False
#         # for j in range(len(nums)):
#         #     print(j)
#         #     if nums[j] == nums[i-1]:
#         #         print(i)
#         #         return True
#         #     else:
#         #         i = i-1
#
#         # return False
#
#         HashSet = set()
#
#         for n in nums:
#             if n in HashSet:
#                 return True
#             else:
#                 HashSet.add(n)
#
#i have written this code but only 29/34 test cases are passing. Not sure why the rest arent
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         test1 = set()
#         test2 = set()
#         for j in t:
#             test1.add(j)
#
#         for i in s:
#             test2.add(i)
#
#         if test1 == test2:
#             return True
#         # for i in s:
#         #     if

#lol this solution works now
# if len(s) == len(t):
#     if sorted(s) == sorted(t):
#         return True
# else:
#     return False
################################### implementing queue with stacks (Real game)
# class MyQueue(object):
#
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#
#     def push(self, x):
#         while self.s1:
#             self.s2.append(self.s1.pop())
#         self.s1.append(x)
#         while self.s2:
#             self.s1.append(self.s2.pop())
#
#     def pop(self):
#         """
#         :rtype: int
#         """
#         return self.s1.pop()
#
#     def peek(self):
#         """
#         :rtype: int
#         """
#         return self.s1[-1]
#
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

### replace elements with greatest on the right side
# class Solution(object):
#     def replaceElements(self, arr):
#         right_max = -1
#         for i in range(len(arr)-1, -1 ,-1 ):
#            new_max = max(arr[i] , right_max)
#            arr[i] = right_max
#            right_max= new_max
#         return arr


##### Leetcode problem - Evaluate reverse polish operation
# class Solution(object):
#     def evalRPN(self, tokens):
#         stack = []
#         for char in tokens:
#             if char == '+':
#                 stack.append(stack.pop() + stack.pop())
#             elif char == '-':
#                  a , b = stack.pop() , stack.pop()
#                  stack.append(b-a)
#             elif char == '*':
#                  stack.append(stack.pop() * stack.pop())
#             elif char == '/':
#                  a , b = stack.pop() , stack.pop()
#                  stack.append(int(int(b)/int(a)))
#             else:
#                 stack.append(int(char))
#         return stack[0]

#################### subsequence wala code (edge case not working ) and its findinga substring , nbeed to look at the locations################
# t = 'axbxcx'
# s = 'acb'
# count = 0
# for i in t:
#     if i in s:
#         count = count + 1
#     else:
#         continue
# if count == len(s):
#     print ('True')
# else:
#     print ('False')

# count = 0
## leetcode code working will all the acceptable test cases
# i = 0
# j = 0
# while i < len(s) and j < len(t):
#     if s[i] == t[j]:
#         # count = count +1
#         i = i +1
#         j = j +1
#     else :
#         j = j +1
#
# if i == len(s):
#     print(True)
# else:
#     print (False)


#################leetcdoe code of adding 1 to the last element################
# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         digits = digits[::-1]
#         one , i = 1 , 0
#
#         while one:
#             if i< len(digits):
#                 if digits[i] == 9:
#                     digits[i] =0
#                 else:
#                     digits[i] += 1
#                     one = 0
#             else:
#                 digits.append(1)
#                 one = 0
#             i += 1
#         return digits[::-1]

#LEETCODE SOLUTION FOR FINDING THE  longest prefix SUBSTRING
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         res = ""  # return this if nothing is in common
#
#         for i in range(len(strs[0])):  # explicitly first
#             for s in strs:
#                 if i == len(s) or s[i] != strs[0][i]:
#                     return res
#             res += strs[0][i]
#
#         return res

############ group anagrams#######################
# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         result = defaultdict(list)
#
#         for i in strs:
#             count = [0] * 26
#
#             for c in i:
#                 count[ord(c) - ord('a')] += 1
#
#             result[tuple(count)].append(i)
#
#         return result.values()

############################ Pascals Triangle####################
# class Solution(object):
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         res = [[1]]
#
#         for i in range(numRows - 1 ):
#             temp = [0] + res[-1] + [0]
#             row = []
#             for j in range(len(res[-1])+ 1):
#                 row.append(temp[j]+ temp[j +1])
#             res.append(row)
#         return res

############Leetcode - Remove an element ############################
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#
#         count = 0
#         for i in range(len(nums)):
#             if val != nums[i]:
#                 nums[count] = nums[i]
#                 count += 1
#         return count
#####################finding unique emails in the entered string array - using built in funnctions
# class Solution(object):
#     def numUniqueEmails(self, emails):
#         """
#         :type emails: List[str]
#         :rtype: int
#         """
#         distinct = set()
#
#         for e in emails:
#             localname , domainname = e.split('@')
#             localname = localname.split('+')[0]
#             localname = localname.replace('.', "")
#             distinct.add((localname , domainname))
#         print(distinct)
#         return len(distinct)
################################################leetcode solution for Isomorphic strings #########################
# class Solution(object):
#     def isIsomorphic(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         mapStoT = {}
#         mapTtoS = {}
#         for i in range(len(s)):
#             char1 = s[i]
#             char2 = t[i]
#             if ((char1 in mapStoT and mapStoT[char1]!= char2) or
#                 (char2 in mapTtoS and mapTtoS[char2]!= char1)):
#                 return False
#             mapStoT[char1] = char2
#             mapTtoS[char2] = char1
#         return True


##################Can plant a flower##############
# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         """
#         :type flowerbed: List[int]
#         :type n: int
#         :rtype: bool
#         """
#         count = 0
#
#         f = [0] + flowerbed + [0]
#
#         for i in range(1, len(f) - 1):
#             if (f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0):
#                 f[i] = 1
#                 n -= 1
#
#         if n <= 0:
#             return True
#         else:
#             return False

            # for i in range(len(flowerbed)):
        #         if (flowerbed[i] == 0 and flowerbed[i+1] == 1):
        #             i+=2
        #             print(i)
        #         else:
        #             count+= 1
        #           #  print (count)


###############################################Majority Element#################################
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         # j1 = 1
#         # for i in range(len(nums)):
#         #     if nums[j1] == nums[i]:
#         #         j1 += 1
#         #         print ('Yolo')
#         #         print (nums[i])
#         #         print(j1)
#
#         # if j1 > (len(nums)/2):
#         #     return j1
#
#         count = {}
#         maxCount = 0
#
#         for n in nums:
#             count[n] = 1 + count.get(n, 1)
#             if count[n] > maxCount:
#                 res = n
#             else:
#                 continue
#             maxCount = max(maxCount, count[n])
#
#         return res
#
#################next greater element#################
# class Solution(object):
#     def nextGreaterElement(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#
#         nums1_Index = {n: i for i, n in enumerate(nums1)}
#         res = [-1] * len(nums1)
#
#         for i in range(len(nums2)):
#             if nums2[i] not in nums1_Index:
#                 continue
#             for j in range(i + 1, len(nums2)):
#                 if nums2[j] > nums2[i]:
#                     index = nums1_Index[nums2[i]]
#                     res[index] = nums2[j]
#                     break
#
#         return res

#####################PIVOT INDEX############################################
# class Solution(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         total = sum(nums)
#         lsum = 0
#         rsum = 0
#         for i in range(len(nums)):
#             rsum = total - nums[i] - lsum
#             print(rsum)
#             if rsum == lsum:
#                 return i
#             lsum = lsum + nums[i]
#
#         return -1

#########
# def findDisappearedNumbers(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     returnList = []
#     n = len(nums)
#     nums = set(sorted(nums))
#     print(nums)
#     # print(nums)
#     for i in range(1, n):
#         if i not in nums:
#             returnList.append(i)
#
#     return returnList

#########################Number of balloons######################
# class Solution(object):
#     def maxNumberOfBalloons(self, text):
#         """
#         :type text: str
#         :rtype: int
#         """
#         Hashmap = Counter(text)
#         HashmapOG = Counter("balloon")
#         res = len(text)
#         print(Hashmap)
#         print(HashmapOG)
#
#         for i in HashmapOG:
#             res = min(res, Hashmap[i] // HashmapOG[i])
#
#         return res
#
#############################Solution to - Word Pattern 1 - Leetcode###############################
# class Solution(object):
#     def wordPattern(self, pattern, s):
#         """
#         :type pattern: str
#         :type s: str
#         :rtype: bool
#         """
#
#         words = s.split()
#         if len(words) != len(pattern):
#             return False
#
#         WordsToChar = {}
#         charToWords = {}
#
#         for c, w in zip(pattern, words):
#             if c in charToWords and charToWords[c] != w:
#                 return False
#             if w in WordsToChar and WordsToChar[w] != c:
#                 return False
#             charToWords[c] = w
#             WordsToChar[w] = c
#
#         return True


########################################Top K frequent elements####################################
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]
#
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)

#
#         for n, c in count.items():
#             freq[c].append(n)

#         print (count)
#         print (freq)
#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     print (res)
# func = Solution()
# func.topKFrequent([1,2,2,2,2,2,2,3,3,3,4,5,6,6,6,6,6,6,6] ,1)
#
#
# nums = {1: "Keval" , 2 : "Harshal" , 3 : 'Meet'}
# array = [[1 ,2 ,3 ], [4 ,5 ,6 ], [7 ,8 ,9 ]]
# nums2={}
#
# j=0
# for i in nums:
#     nums[i]=array[j]
#     j+=1
# j=0
# for i in list(nums):
#     nums2[i+1]=array[j]
#     j+=1
#
# # nums[i].replace(nums[i] , "This is updated")
# print(nums2)

###############Single Number##################################################################################################################################
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         hashmap = {}
#         for  i  in range(len(nums)):
#             if nums[i] not in hashmap:
#                 hashmap[nums[i]]=1
#             else:
#                 hashmap[nums[i]]=hashmap[nums[i]]+1
#         for i in hashmap:
#             if hashmap[i]==1:
#                 return i
#
#
########################################Contains Duplicate 2#############################
# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if (i == j):
#                     continue
#                 if nums[i] == nums[j] and abs(i - j) <= k:
#                     return True
#
#         return False
#

##############################Contains Duplicate 2################################# (optimal view)
# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         Hashmap = {}
#         for index, key in enumerate(nums):
#             if (key in Hashmap and index - Hashmap[key] <= k):
#                 return True
#
#             Hashmap[key] = index
#
#         return False
#
#



###################contains duplicate revised##################################
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#
#         numspro = set()
#         for i in range(len(nums)):
#             numspro.add(nums[i])
#
#         if len(nums) == len(numspro):
#             return False
#
#         return True
#######valid anagram###################
# import defaultdict from collections
# d = defaultdict()
#     for i in s:
#         if i in d:
#                 d[i] +=1
#             else:
#                 d[i] = 1
#
#         for i in t:
#             if i in t:
#                 d[i] = d[i] - 1
#             else:
#                 d[i]=1
#         for i in d:
#             if d[i] > 0:
#                 return False
#
#         return True
################################################Kth largest element in an array#########################


#########################wrod patterns##################



















#############deleting the unsorted columns##################################
# class Solution:
#     def minDeletionSize(self, strs: List[str]) -> int:
#         del_col = 0
#         for c in range(len(strs[0])):
#             for r in range(len(strs)-1):
#                 if strs[r][c] > strs[r+1][c]:
#                     del_col += 1
#                     break
#         return del_col
#
#

#########################finding a pivot#######################
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         total = sum(nums)
#         rightsum = 0
#         leftsum = 0
#         for i in range(len(nums)):
#             rightsum = total - leftsum - nums[i]
#             if rightsum == leftsum:
#                 return i
#             leftsum = leftsum + nums[i]
#
#         return -1
#
##############daily coding challenge leetcode####################
# class Solution:
#     def minimumRounds(self, tasks: List[int]) -> int:
#         frequency = Counter(tasks)
#         print(frequency)
#         print (frequency.values())
#         res = 0
#         for freq in frequency.values():
#             if freq == 1:
#                 return -1
#             elif (freq-2) % 3 == 0:
#                 res += (freq-2) // 3 + 1
#             elif (freq - 4) % 3 == 0:
#                 res += (freq - 4) // 3 +2
#             elif freq % 3 == 0:
#                 res += freq // 3
#             else:
#                 res += freq // 2
#         return res

#######################adding binary problem##########################
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a = list(a)
#         b = list(b)
#         carry = 0
#         result = ''
#
#         while a or b or carry:
#             if a:
#                 carry += int(a.pop())
#                 print(carry)
#             if b:
#                 carry += int(b.pop())
#                 print(carry)
#
#             result += str(carry % 2)
#             carry //= 2
#             print(carry)
#
#         print(result)
#         return result[::-1]


########################leetcode daily problem (solution not working)#####################
# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         array = []
#         for i in range(len(points)):
#             # print(len(points[i]))
#             for j in range(len(points[i]) - 1):
#                 array.append(abs(points[i][j] - points[i][j + 1]))
#
#         print(array)
#         count = 0
#         for i in range(len(array) - 1):
#             if array[i] <= array[i + 1]:
#                 count += 1
#
#         print(count)
#         return count
##################################leetcode daily problem#################### working solution
# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         points = sorted(points, key=lambda x: x[1])
#         count = 0
#         ending = float('-inf')
#
#         for balloon in points:
#             if balloon[0] > ending:
#                 count += 1
#                 ending = balloon[1]
#
#         return count
##########################leetcode daily problem###############################
# class Solution:
#     def maxIceCream(self, costs: List[int], coins: int) -> int:
#         # Store ice cream costs in increasing order.
#         costs.sort()
#         n, icecream = len(costs), 0
#
#         # Pick ice creams till we can.
#         while icecream < n and costs[icecream] <= coins:
#             # We can buy this icecream, reduce the cost from the coins.
#             coins -= costs[icecream]
#             icecream += 1
#
#         return icecream

###################square root findinf with the binary sort##################
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x <= 1: return x
#
#         start = 2
#         end = x
#
#         # Apply Binary Search since range 1 to x is in sorted order
#         while start <= end:
#             mid = start + (end - start) // 2
#
#             square = mid * mid
#             # If square of a number is equal to x, we got the square root
#             if square == x: return mid
#             # If square of a number if less than x, go for a bigger number
#             if square < x:
#                 start = mid + 1
#             # If square of a number if more than x, go for a smaller number
#             else:
#                 end = mid - 1
#                 print(end)
#
#         # If the number is not a perfect square, return the value "end"
#         return end
#leetcode my solution working#### medium
# class Solution:
#     def maxIceCream(self, costs: List[int], coins: int) -> int:
#         costs = sorted(costs)
#         num = 0
#         print(costs)
#         for i in costs:
#             if i <= coins:
#                 coins = coins - i
#                 num = num + 1
#                 print(num)
#
#         return num

################leetcode gas station##########################
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         if sum(gas) < sum(cost):
#             return -1
#
#         res = 0
#         total = 0
#         for i in range(len(cost)):
#             total = total + (gas[i] - cost[i])
#
#             if total < 0:
#                 total = 0
#                 res = i + 1
#
#         return res
# #         n, total_surplus, surplus, start = len(gas), 0, 0, 0
#
# #         for i in range(n):
# #             total_surplus += gas[i] - cost[i]
# #             surplus += gas[i] - cost[i]
# #             if surplus < 0:
# #                 surplus = 0
# #                 start = i + 1
# #         return -1 if (total_surplus < 0) else start
##########################################################################matrix multiplication to understand how a 2d array works##########
# print('Entet the number of rows')
# num_rows = int(input())
# row = []
# for  i in range(num_rows):
#     print (f"Enter the number of elements in  row:")
#     element = int(input())
#     row.append(element)
#
# print('Entet the number of cols')
# num_col = int(input())
# matrix = [[]]
# for  i in range(num_col):
#     print (f"Enter the number of elements in  row:")
#     element = int(input())
#     matrix.append[i[element]]
#
# print (matrix)
##############################################valid soduku algorithm#####################
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         columns = collections.defaultdict(set)
#         rows = collections.defaultdict(set)
#         sqaure = collections.defaultdict(set)
#
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
#                 if (board[r][c] in columns[c] or board[r][c] in rows[r] or board[r][c] in sqaure[(r // 3, c // 3)]):
#                     return False
#                 columns[c].add(board[r][c])
#                 rows[r].add(board[r][c])
#                 sqaure[(r // 3, c // 3)].add(board[r][c])
#         print(columns)
#         print(rows)
#         print(sqaure)
#
#         return True
######################the cdoe which is not working###############
#         ##accessing the rows
#
#         # for i in range(len(board)):
#         #     for j in range(len(board)-1):
#         #         if board[i][j] == board[i][j+1]:
#         #             return False
#         #         if board[j][i] == '.' or board[j][i] <= '9':
#         #             return True
#
#         ##accessing the columns
#
#         # for i in range(len(board)):
#         #     for j in range(len(board)-1):
#         #         if board[j][i] == board[j+1][i]:
#         #             return False
#         #         if board[j][i] == '.' or board[j][i] <= '9':
#         #             return True

#####################Longest Consequetive Sequence#####################
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#
#         if len(nums) == 0:
#             return 0
#
#         numpro = sorted(nums)
#         print(numpro)
#         count = 1
#         for i in range(len(numpro) - 1):
#             print(numpro[i])
#             print(numpro[i] + 1)
#             if numpro[i] + 1 == numpro[i + 1]:
#                 count += 1
#
#         return count
###############################################################two sum revision#########
# nums = [3,6,7,8,9,10 ]
# target =  10
#
# for i in range(len(nums)):
#     for j in range(1 , len(nums)):
#         if nums[i] == target-nums[j]:
#             print(i , j )


#################sorting the colours##################
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] > nums[j]:
#                     nums[i], nums[j] = nums[j], nums[i]
#         print(nums)

#######leetcode for finding the sqaure of the array and sort it ###
# class Solution(object):
#     def sortedSquares(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#
#         nums1 = []
#
#         for i in range(len(nums)):
#             nums1.append((nums[i]) * (nums[i]))
#
#         return sorted(nums1)
#
##################leetcode#############################

#######################training a model in javascript###################
# / *If
# you
# 're feeling fancy you can add interactivity
# to
# your
# site
# with Javascript * /
#
# // prints
# "hi" in the
# browser
# 's dev tools console
# console.log('hi');
# async function
# getData()
# {
#     const
# carsDataResponse = await fetch('https://storage.googleapis.com/tfjs-tutorials/carsData.json');
# const
# carsData = await carsDataResponse.json();
# const
# cleaned = carsData.map(car= > ({
#     mpg: car.Miles_per_Gallon,
#     horsepower: car.Horsepower,
# }))
# .filter(car= > (car.mpg != null & & car.horsepower != null));
#
# return cleaned;
# }
#
# async function
# run()
# {
# // Load and plot
# the
# original
# input
# data
# that
# we
# are
# going
# to
# train
# on.
# const
# data = await getData();
# const
# values = data.map(d= > ({
#     x: d.horsepower,
#     y: d.mpg,
# }));
#
# tfvis.render.scatterplot(
#     {name: 'Horsepower v MPG'},
#     {values},
#     {
#         xLabel: 'Horsepower',
#         yLabel: 'MPG',
#         height: 300
#     }
# );
#
# const
# model = createModel();
# tfvis.show.modelSummary({name: 'Model Summary'}, model);
#
# // Convert
# the
# data
# to
# a
# form
# we
# can
# use
# for training.
#     const
# tensorData = convertToTensor(data);
# const
# {inputs, labels} = tensorData;
#
# // Train
# the
# model
# await trainModel(model, inputs, labels);
# console.log('Done Training');
# }
#
# function
# createModel()
# {
# // Create
# a
# sequential
# model
# const
# model = tf.sequential();
#
# // Add
# a
# single
# input
# layer
# model.add(tf.layers.dense({inputShape: [1], units: 1, useBias: true}));
#
# // Add
# an
# output
# layer
# model.add(tf.layers.dense({units: 1, useBias: true}));
#
# return model;
# }
#
# function
# convertToTensor(data)
# {
# // Wrapping
# these
# calculations in a
# tidy
# will
# dispose
# any
# // intermediate
# tensors.
#
# return tf.tidy(() = > {
#                       // Step
# 1.
# Shuffle
# the
# data
# tf.util.shuffle(data);
#
# // Step
# 2.
# Convert
# data
# to
# Tensor
# const
# inputs = data.map(d= > d.horsepower)
# const
# labels = data.map(d= > d.mpg);
#
# const
# inputTensor = tf.tensor2d(inputs, [inputs.length, 1]);
# const
# labelTensor = tf.tensor2d(labels, [labels.length, 1]);
#
# // Step
# 3.
# Normalize
# the
# data
# to
# the
# range
# 0 - 1
# using
# min - max
# scaling
# const
# inputMax = inputTensor.max();
# const
# inputMin = inputTensor.min();
# const
# labelMax = labelTensor.max();
# const
# labelMin = labelTensor.min();
#
# const
# normalizedInputs = inputTensor.sub(inputMin).div(inputMax.sub(inputMin));
# const
# normalizedLabels = labelTensor.sub(labelMin).div(labelMax.sub(labelMin));
#
# return {
#            inputs: normalizedInputs,
#            labels: normalizedLabels,
#        // Return
# the
# min / max
# bounds
# so
# we
# can
# use
# them
# later.
#     inputMax,
# inputMin,
# labelMax,
# labelMin,
# }
# });
# }
# async function
# trainModel(model, inputs, labels)
# {
# // Prepare
# the
# model
# for training.
#         model.compile({
#     optimizer: tf.train.adam(),
#     loss: tf.losses.meanSquaredError,
#     metrics: ['mse'],
#     });
#
#     const
#     batchSize = 32;
#     const
#     epochs = 50;
#
#     return await model.fit(inputs, labels, {
#         batchSize,
#         epochs,
#         shuffle: true,
#                  callbacks: tfvis.show.fitCallbacks(
#         {name: 'Training Performance'},
#         ['loss', 'mse'],
#         {height: 200, callbacks: ['onEpochEnd']}
#     )
#     });
#     }
#
#     function
#     testModel(model, inputData, normalizationData)
#     {
#     const
#     {inputMax, inputMin, labelMin, labelMax} = normalizationData;
#
#     // Generate
#     predictions
#     for a uniform range of numbers between 0 and 1;
#     // We
#     un - normalize
#     the
#     data
#     by
#     doing
#     the
#     inverse
#     of
#     the
#     min - max
#     scaling
#     // that
#     we
#     did
#     earlier.
#     const[xs, preds] = tf.tidy(() = > {
#
#         const
#     xsNorm = tf.linspace(0, 1, 100);
#     const
#     predictions = model.predict(xsNorm.reshape([100, 1]));
#
#     const
#     unNormXs = xsNorm \
#         .mul(inputMax.sub(inputMin)) \
#         .add(inputMin);
#
#     const
#     unNormPreds = predictions \
#         .mul(labelMax.sub(labelMin)) \
#         .add(labelMin);
#
#     // Un - normalize
#     the
#     data
#     return [unNormXs.dataSync(), unNormPreds.dataSync()];
#     });
#
#
#     const
#     predictedPoints = Array.
#     from
#
#     (xs).map((val, i) = > {
#     return {x: val, y: preds[i]}
# });
#
# const
# originalPoints = inputData.map(d= > ({
#     x: d.horsepower, y: d.mpg,
# }));
#
#
# tfvis.render.scatterplot(
#     {name: 'Model Predictions vs Original Data'},
#     {values: [originalPoints, predictedPoints], series: ['original', 'predicted']},
#     {
# xLabel: 'Horsepower',
# yLabel: 'MPG',
# height: 300
# }
# );
# }
#
# const
# model = tf.sequential();
# model.add(tf.layers.dense({inputShape: [1], units: 1, useBias: true}));
# model.add(tf.layers.dense({units: 1}));
#
# document.addEventListener('DOMContentLoaded', run);
# / *If
# you
# 're feeling fancy you can add interactivity
# to
# your
# site
# with Javascript * /
#
#      // prints "hi" in the browser's dev tools console
# console.log('hi');
# async function getData() {
# const carsDataResponse = await fetch('https://storage.googleapis.com/tfjs-tutorials/carsData.json');
# const carsData = await carsDataResponse.json();
# const cleaned = carsData.map(car = > ({
# mpg: car.Miles_per_Gallon,
#      horsepower: car.Horsepower,
# }))
# .filter(car= > (car.mpg != null & & car.horsepower != null));
#
# return cleaned;
# }
#
# async function
# run()
# {
# // Load and plot
# the
# original
# input
# data
# that
# we
# are
# going
# to
# train
# on.
# const
# data = await getData();
# const
# values = data.map(d= > ({
#     x: d.horsepower,
#     y: d.mpg,
# }));
#
# tfvis.render.scatterplot(
#     {name: 'Horsepower v MPG'},
#     {values},
#     {
#         xLabel: 'Horsepower',
#         yLabel: 'MPG',
#         height: 300
#     }
# );
#
# const
# model = createModel();
# tfvis.show.modelSummary({name: 'Model Summary'}, model);
#
# // Convert
# the
# data
# to
# a
# form
# we
# can
# use
# for training.
#     const
# tensorData = convertToTensor(data);
# const
# {inputs, labels} = tensorData;
#
# // Train
# the
# model
# await trainModel(model, inputs, labels);
# console.log('Done Training');
# }
#
# function
# createModel()
# {
# // Create
# a
# sequential
# model
# const
# model = tf.sequential();
#
# // Add
# a
# single
# input
# layer
# model.add(tf.layers.dense({inputShape: [1], units: 1, useBias: true}));
#
# // Add
# an
# output
# layer
# model.add(tf.layers.dense({units: 1, useBias: true}));
#
# return model;
# }
#
# function
# convertToTensor(data)
# {
# // Wrapping
# these
# calculations in a
# tidy
# will
# dispose
# any
# // intermediate
# tensors.
#
# return tf.tidy(() = > {
#                       // Step
# 1.
# Shuffle
# the
# data
# tf.util.shuffle(data);
#
# // Step
# 2.
# Convert
# data
# to
# Tensor
# const
# inputs = data.map(d= > d.horsepower)
# const
# labels = data.map(d= > d.mpg);
#
# const
# inputTensor = tf.tensor2d(inputs, [inputs.length, 1]);
# const
# labelTensor = tf.tensor2d(labels, [labels.length, 1]);
#
# // Step
# 3.
# Normalize
# the
# data
# to
# the
# range
# 0 - 1
# using
# min - max
# scaling
# const
# inputMax = inputTensor.max();
# const
# inputMin = inputTensor.min();
# const
# labelMax = labelTensor.max();
# const
# labelMin = labelTensor.min();
#
# const
# normalizedInputs = inputTensor.sub(inputMin).div(inputMax.sub(inputMin));
# const
# normalizedLabels = labelTensor.sub(labelMin).div(labelMax.sub(labelMin));
#
# return {
#            inputs: normalizedInputs,
#            labels: normalizedLabels,
#        // Return
# the
# min / max
# bounds
# so
# we
# can
# use
# them
# later.
#     inputMax,
# inputMin,
# labelMax,
# labelMin,
# }
# });
# }
# async function
# trainModel(model, inputs, labels)
# {
# // Prepare
# the
# model
# for training.
#         model.compile({
#     optimizer: tf.train.adam(),
#     loss: tf.losses.meanSquaredError,
#     metrics: ['mse'],
#     });
#
#     const
#     batchSize = 32;
#     const
#     epochs = 50;
#
#     return await model.fit(inputs, labels, {
#         batchSize,
#         epochs,
#         shuffle: true,
#                  callbacks: tfvis.show.fitCallbacks(
#         {name: 'Training Performance'},
#         ['loss', 'mse'],
#         {height: 200, callbacks: ['onEpochEnd']}
#     )
#     });
#     }
#
#     function
#     testModel(model, inputData, normalizationData)
#     {
#     const
#     {inputMax, inputMin, labelMin, labelMax} = normalizationData;
#
#     // Generate
#     predictions
#     for a uniform range of numbers between 0 and 1;
#     // We
#     un - normalize
#     the
#     data
#     by
#     doing
#     the
#     inverse
#     of
#     the
#     min - max
#     scaling
#     // that
#     we
#     did
#     earlier.
#     const[xs, preds] = tf.tidy(() = > {
#
#         const
#     xsNorm = tf.linspace(0, 1, 100);
#     const
#     predictions = model.predict(xsNorm.reshape([100, 1]));
#
#     const
#     unNormXs = xsNorm \
#         .mul(inputMax.sub(inputMin)) \
#         .add(inputMin);
#
#     const
#     unNormPreds = predictions \
#         .mul(labelMax.sub(labelMin)) \
#         .add(labelMin);
#
#     // Un - normalize
#     the
#     data
#     return [unNormXs.dataSync(), unNormPreds.dataSync()];
#     });
#
#
#     const
#     predictedPoints = Array.
#     from
#
#     (xs).map((val, i) = > {
#     return {x: val, y: preds[i]}
# });
#
# const
# originalPoints = inputData.map(d= > ({
#     x: d.horsepower, y: d.mpg,
# }));
#
#
# tfvis.render.scatterplot(
#     {name: 'Model Predictions vs Original Data'},
#     {values: [originalPoints, predictedPoints], series: ['original', 'predicted']},
#     {
# xLabel: 'Horsepower',
# yLabel: 'MPG',
# height: 300
# }
# );
# }
#
# const
# model = tf.sequential();
# model.add(tf.layers.dense({inputShape: [1], units: 1, useBias: true}));
# model.add(tf.layers.dense({units: 1}));
#
# document.addEventListener('DOMContentLoaded', run);


##################leetcoe converting an to integer#########My solution working only for 1 test case
# class Solution(object):
#     def myAtoi(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         yolo = []
#         for i in s:
#             if i == ' ' or i == '_' or i == '-' or i == '.':
#                 print('If satisfied')
#                 continue
#             else:
#                 yolo.append(i)
#                 print('Else satisdie')
#
#         data = ''
#         for i in yolo:
#             data += i
#
#         return (int(data))
####################workin solution##############(need to revise)
# class Solution(object):
#     def myAtoi(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         s = s.lstrip()
#         print(s)
#
#         if not s:
#             return 0
#
#         if len(s) == 1 and not s[0].isdigit():
#             return 0
#
#         i = 0
#
#         sign = 1
#
#         if s[i] == "+":
#             i += 1
#         if s[i] == "-":
#             sign = -1
#             i += 1
#
#         if i == 2:
#             return 0
#
#         parsed = 0
#
#         while i < len(s):
#             if not (s[i]).isdigit():
#                 break
#             else:
#                 parsed = parsed * 10 + int(s[i])
#             i += 1
#         parsed = sign * parsed
#         if parsed > 2 ** 31 - 1:
#             return 2 ** 31 - 1
#         elif parsed <= -2 ** 31:
#             return -2 ** 31
#         else:
#             return parsed

##############Finding the index of the first occurence of the string#####################
# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if needle == "":
#             return 0
#
#         for i in range(len(haystack) + 1 - len(needle)):
#             for j in range(len(needle)):
#                 if haystack[i + j] != needle[j]:
#                     break
#                 if j == len(needle) - 1:
#                     return i
#
#         return -1

#######################Finding first palindromic string in an array##################
# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
#         ans = 0
#
#         for i in words:
#             if i == i[::-1]:
#                 return i
#             elif i != i[::-1]:
#                 continue
#
#         return ('')
#

################YOU CANNNNNNOT DO THE ARRAY MANIPULATION TECHNIQUES WITHOUT IMPORTING ARRAY * #######################

######################CONTAINER WITH MOST WATER########################################################## (Passing 4 twst cases out of the 16) {my solution}
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#
#         for i in range(len(height)):
#             for j in range(i + 1, len(height) + 1):
#                 print(f'This is ith height {height[i]}')
#                 print(f'This is jth height {height[j - 1]}')
#                 if i < len(height) and j < len(height):
#                     ans = max(((height[i] * height[j - i]) * (j - i)), ((height[i] * height[j]) * (j - i)))
#                 else:
#                     ans = max(ans, 0)
#
#         return (ans)


#############right brute force approach###################
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#
#         result = 0
#
#         for left in range(len(height)):
#             for right in range(left + 1, len(height)):
#                 area = (right - left) * min(height[left], height[right])
#                 result = max(result, area)
#
#         return result

#########################working solution on leetcode#####################
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#
#         res = 0
#
#         left = 0
#         right = len(height) - 1
#         while left < right:
#             area = (right - left) * min(height[left], height[right])
#             res = max(area, res)
#
#             if height[right] > height[left]:
#                 left += 1
#             else:
#                 right -= 1
#
#         return res
#
# print('Enter your date of birth')
# dob = input()
# nums =[]
# for i in dob:
#     j = int(i)
#     nums.append(j)
# ans = 0
# for z in range(len(nums)):
#     ans = ans+ nums[z]
#
# ans = ans%10
# ans = ans + ans
# print(ans)

############leetcode buying and selling a stock############
# class Solution(object):
#     def maxProfit(self, prices):
#
#         if len(prices) == 0:
#             return 0
#
#         max = prices[len(prices) - 1]
#         profit = 0
#
#         for item in prices[::-1]:
#             if max - item > profit:
#                 profit = max - item
#             if item > max:
#                 max = item
#
#         return profit
#
###############leetcode problem 39 - combination sum############# solution is working only for the example test cases
 # class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#
#         num = []
#
#         for i in range(len(candidates)):
#             if candidates[i] == target:
#                 num.append(candidates[i])
#                 continue
#             for j in range(1, len(candidates)):
#                 if candidates[i] + candidates[j] < target:
#                     print('first if executed')
#                     sub = target - (candidates[i] + candidates[j])
#                     if sub in candidates:
#                         print('if ke andar if executed')
#                         num.append(sub)
#                         num.append(candidates[i])
#                         num.append(candidates[j])
#                     else:
#                         print('else executed')
#                         continue
#
#         candidates.append(num)
#         print(candidates)


############################insert interval########
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         result = []
#         for i in intervals:
#             if i[1] < newInterval[0]:
#                 result.append(i)
#
#             elif i[0] > newInterval[1]:
#                 result.append(newInterval)
#                 newInterval = i
#
#             elif i[1] >= newInterval[0] or i[0] <= newInterval[1]:
#                 newInterval[0] = min(i[0], newInterval[0])
#                 newInterval[1] = max(newInterval[1], i[1])
#
#         result.append(newInterval);
#         return result


########Make array zero by subtracting the elements###################
# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         nums = set(nums)
#         if 0 in nums:
#             return(len(nums)-1)
#         else:
#             return(len(nums))

############minimum path sum#################
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j != 0:
#                     grid[i][j] = grid[i][j] + grid[i][j - 1]
#                 elif i != 0 and j == 0:
#                     grid[i][j] = grid[i][j] + grid[i - 1][j];
#                 elif i > 0 and j > 0:
#                     grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]
#
#         return grid[m - 1][n - 1]
# class Solution: (first solution passsing 57 test cases)
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in nums:
#                 return [i, nums.index(complement)]
#solution passing all the test cases
        # hashmap = {}
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap:
        #         return [i, hashmap[complement]]
        #     hashmap[nums[i]] = i
###########word search - my code which is not working##########################
#m = len(board)
#         n = len(board[0])
# #         wordlist = []
# #         for i in word:
# #             wordlist.append(i)

# #         print(wordlist)
#         count =0
#         for i in range(m):
#             for j in range(n):
#               #  print(board[i][j])
#                 if board[i][j] in word and (board[i][j-1] or board[i-1][j] or board[i-1][j-1] or board[i+1][j+1] in word):
#                         count+=1
#                         print(count)
#                 else:
#                     print('else executed')
#################leetcode code working###################
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         ROWS, COLS = len(board), len(board[0])
#         path = set()
#
#         def dfs(r, c, i):
#             if i == len(word):
#                 return True
#             if (
#                     min(r, c) < 0
#                     or r >= ROWS
#                     or c >= COLS
#                     or word[i] != board[r][c]
#                     or (r, c) in path
#             ):
#                 return False
#             path.add((r, c))
#             res = (
#                     dfs(r + 1, c, i + 1)
#                     or dfs(r - 1, c, i + 1)
#                     or dfs(r, c + 1, i + 1)
#                     or dfs(r, c - 1, i + 1)
#             )
#             path.remove((r, c))
#             return res
#
#         # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
#         count = defaultdict(int, sum(map(Counter, board), Counter()))
#         if count[word[0]] > count[word[-1]]:
#             word = word[::-1]
#
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if dfs(r, c, 0):
#                     return True
#         return False
###########shift the zeroes to the last in the existing arrray##############
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 count += 1
#
#         for i in range(count):
#             nums.remove(0)
#             nums.append(0)
#

########Brickwall solution#####################
# class Solution:
#     def leastBricks(self, wall: List[List[int]]) -> int:
#         edge_count = {}
#         for row in wall:
#             width = 0
#             for brick in row[:-1]:
#                 width += brick
#                 if width in edge_count:
#                     edge_count[width] += 1
#                 else:
#                     edge_count[width] = 1
#         if not edge_count:
#             return len(wall)
#
#         return len(wall) - max(edge_count.values())

###############slowest key#################
# class Solution:
#     def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
#
#         max_ans = releaseTimes[0]
#         ans = 0
#         char = keysPressed[0]
#         for i in range(1, len(releaseTimes)):
#             ans = releaseTimes[i] - releaseTimes[i - 1]
#             print(ans, keysPressed[i])
#             if ans >= max_ans:
#                 if ans == max_ans:
#                     if ord(char) < ord(keysPressed[i]):
#                         char = keysPressed[i]
#                         print(char)
#                 else:
#                     char = keysPressed[i]
#                 max_ans = ans
#
#         return char
###################Range sum Querry#################
# class NumArray(object):
#     def __init__(self, nums):
#         l = [nums[0]]  # store first element of the array to start prefix sum
#         for i in range(1, len(nums)):
#             l.append(l[i - 1] + nums[i])  # implement prefix sum for each element
#         self.arr = l
#
#     def sumRange(self, left, right):
#         if (
#                 left != 0):  # Apply the logic of prefix sum to get the sum of elements between and including left and right.
#             return (self.arr[right] - self.arr[left - 1])
#         else:  # in case left is 0,the sum in the 'right' position will give the total sum required
#             return (self.arr[right])
#################range sum querry with inbuilt functions###############
# class Codec:
#     def __init__(self):
#         self.encodeMap = {}
#         self.decodeMap = {}
#         self.base = "http://tinyurl.com/"
#
#     def encode(self, longUrl: str) -> str:
#         """Encodes a URL to a shortened URL.
#         """
#         if longUrl not in self.encodeMap:
#             shortUrl = self.base + str(len(self.encodeMap) + 1)
#             self.encodeMap[longUrl] = shortUrl
#             self.decodeMap[shortUrl] = longUrl
#         return self.encodeMap[longUrl]
#
#     def decode(self, shortUrl: str) -> str:
#         """Decodes a shortened URL to its original URL.
#         """
#         return self.decodeMap[shortUrl]

############leetcode - finding interesection of array#####################
# class Solution(object):
#     def intersect(self, nums1, nums2):
#
#         nums1, nums2 = sorted(nums1), sorted(nums2)
#         pt1 = pt2 = 0
#         output = []
#
#         while True:
#             try:
#                 if nums1[pt1] > nums2[pt2]:
#                     pt2 += 1
#                 elif nums1[pt1] < nums2[pt2]:
#                     pt1 += 1
#                 else:
#                     output.append(nums1[pt1])
#                     pt1 += 1
#                     pt2 += 1
#             except IndexError:
#                 break
#
#         return output

###########leetcode - interection of an array (unique values)###########
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#
#         output = []
#
#         for i in nums1:
#             if i in nums2:
#                 output.append(i)
#             else:
#                 continue
#
#         output = set(output)
#
#         return output
