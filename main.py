###neetcode two pointer
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#
#         ans = []
#         for i in s:
#             if i.isalnum():
#                 i = i.upper()
#                 ans.append(i)
#
<<<<<<< HEAD
#         return sum(ans)
#######divisor game - Lol##########
# class Solution:
#     def divisorGame(self, n: int) -> bool:
#         return n%2==0
=======
#         print(ans)
#         print(ans[::-1])
#         if ans == ans[::-1]:
#             return True
#         else:
#             return False
<<<<<<< HEAD

#####TWO POINTER - Two sum 2 (input array is sorted)
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#
#         l, r = 0, len(numbers) - 1
#         while l < r:
#             s = numbers[l] + numbers[r]
#             if s == target:
#                 return [l + 1, r + 1]
#             elif s < target:
#                 l += 1
#             else:
#                 r -= 1
#
# #         ans = []
# #         for i in numbers:
# #             j = target- i
# #             if j in numbers:
# #                 k = numbers.index(j)
# #                 j = i
# #                 ans.append(k+1)
#
#
# #         print(sorted(ans))
#
=======
>>>>>>> 43419b07b410a8f450f93411459d83e8d070dc82
>>>>>>> 760a5e4241f84743a7d95289956ee7289445363d
