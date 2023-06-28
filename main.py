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
#

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


#########valid parentheses########
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

##########find the highest altitude
# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         ans = [0]
#
#         for i in range(len(gain)):
#             ans.append(gain[i] + ans[i])
#
#         print(ans)
#         return max(ans)

###############Minimum number of seats to move everyone

# class Solution:
#     def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
#         ans = []
#         seats = sorted(seats)
#         students = sorted(students)
#
#         for i in range(0, len(students)):
#             j = students[i] - seats[i]
#             ans.append(abs(j))
#
#         print(sum(ans))
#         return sum(ans)
#
#
####trapping rainwater //leetcode hard


# class Solution:
#     def trap(self, height: List[int]) -> int:
#
#         left, right = 0, len(height) - 1
#         maxLeft, maxRight = height[left], height[right]
#         result = 0
#
#         while left < right:
#             if maxLeft < maxRight:
#                 left = left + 1
#                 maxLeft = max(maxLeft, height[left])
#                 result += maxLeft - height[left]
#             else:
#                 right = right - 1
#                 maxRight = max(maxRight, height[right])
#                 result += maxRight - height[right]
#
#         return result



#sum of all off length subarrays
# class Solution:
#     def sumOddLengthSubarrays(self, arr: List[int]) -> int:
#         n = len(arr)
#         answer = 0
#         for left in range(n):
#             current_sum = 0
#             for right in range(left, n):
#                 current_sum += arr[right]
#                 answer += current_sum if (right - left + 1) % 2 == 1  else 0
#         return answer


###neighter minimum nor maximum
#
# class Solution:
#     def findNonMinOrMax(self, nums: List[int]) -> int:
#
#         if len(nums) == 2 or len(nums) == 1 or len(nums) == 0:
#             return -1
#
#         num1 = max(nums)
#         num2 = min(nums)
#
#         for i in nums:
#             if i != num1 and i != num2:
#                 return i
#
#
#

