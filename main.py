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
#
#
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
# # brute force approach , maximum time limit exceeded
# #         result = 0
#
# #         for left in range(len(height)):
# #             for right in range(left+1 , len(height)):
# #                 area = (right - left) * min(height[left], height[right])
# #                 result = max(result, area)
#
# #         return result
#
# #         for i in range(len(height)):
# #             for  j in range(i+1 , len(height)+1):
# #                 print(f'This is ith height {height[i]}')
# #                 print(f'This is jth height {height[j-1]}')
# #                 if i < len(height) and j < len(height):
# #                     ans = max(((height[i]*height[j-i])*(j-i)) ,((height[i]*height[j])*(j-i)))
# #                 else :
# #                     ans = max(ans, 0)
#
#
# #         return(ans)
