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

##########count the negative numbers in a matrix
# class Solution:
    # def countNegatives(self, grid: List[List[int]]) -> int:
    #
    #     ans = []
    #
    #     count = 0
    #
    #     for i in range(0 , len(grid)):
    #         for j in range( 0 , len(grid[i])):
    #             print (grid[i][j])
    #             ans.append(grid[i][j])
    #
    #
    #     print (ans)
    #     for i in ans:
    #         if i < 0:
    #             count += 1
    #
    #     return count

###########maximum count of positive and negative integer#
# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         pos = 0
#         neg = 0
#
#         for i in nums:
#             if i > 0:
#                 pos += 1
#             if i < 0:
#                 neg += 1
#             else:
#                 pos = pos
#                 neg = neg
#
#         print(f"Pos {pos}")
#         print(neg)
#         print(max(neg, pos))
#         return (max(neg, pos))
#

################missing number
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         l = len(nums)
#         nums = sorted(nums)
#         real_ans = 0
#
#         ans = []
#         for i in range(1, l + 1):
#             ans.append(i)
#
#         for i in ans:
#             if i not in nums:
#                 real_ans = i
#
#         print(type(real_ans))
#         return real_ans
#         # return real_ans


##################height checker##
# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#
#         expected = sorted(heights)
#
#         print(expected)
#         ans = 0
#         print(len(heights))
#         for i in range(0, len(heights)):
#             print(i)
#             print(expected[i])
#             print(heights[i])
#             if expected[i] != heights[i]:
#                 ans += 1
#
#         return ans

####### Count the number of consistent strings###########
#
# class Solution:
#     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#
#         count = 0
#
#         for word in words:
#             for ch in word:
#                 if ch not in allowed:
#                     count += 1
#                     break
#
#         print(len(words) - count)
#         return len(words) - count

##########Count the number of even digit numbers in an array#########
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         numspro = []
#
#         count = 0
#
#         for i in nums:
#             numspro.append(str(i))
#
#         print(numspro)
#         for j in numspro:
#             if len(j) % 2 == 0:
#                 count += 1
#
#         print(count)
#         return count

################printinh the sum of unique elements###########
#
# class Solution:
#     def sumOfUnique(self, nums: List[int]) -> int:
#
#         result = 0
#         dup = set()
#         unique = set()
#
#         for ele in nums:
#             if not (ele in unique or ele in dup):
#                 unique.add(ele)
#             elif ele in unique:
#                 unique.discard(ele)
#                 dup.add(ele)
#
#         for elements in unique:
#             result += elements
#
#         print(dup)
#
#         print(unique)
#         return result
#
# #         duplicate = set()
# #         unique = set()
#
#
# #         for element in nums:
# #             if element not in unique or element not in duplicate:
# #                 unique.add(element)
# #                 print (element)
#
# #             elif element in unique:
# #                 duplicate.add(element)
# #                 unique.discard(element)
#
#
# #         print(unique)
# #         print(duplicate)

##busy student###########
# class Solution:
#     def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
#
#         count = 0
#         for i in range(0, len(startTime)):
#             if startTime[i] <= queryTime and endTime[i] >= queryTime:
#                 count += 1
#
#         return count
#     #         count = 0
#
# #         if len(startTime) == 1 or startTime[0] - endTime[0] == 0 :
# #                       print (count)
# #             if startTime[0] - endTime[0] == queryTime:
# #                 count =1
# #                 print (f"Len 1 eala count {count}")
# #             return count
#
# #         else:
# #             for i in range(0 , len(startTime)):
# #                 if endTime[i] - startTime[i] == queryTime :
# #                       count +=1
# #             return (count)
#
#
###shuffle string#####
# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         # string_arr = []
#
#         res = [''] * len(s)
#
#         for i in range(len(s)):
#             res[indices[i]] = s[i]
#
#         result = ''.join(res)
#         print(result)
#
#         return result
####################finding the maximum area of the triangle from the given co-ordinates########

# class Solution:
#     def largestTriangleArea(self, points: List[List[int]]) -> float:
#
#         area = 0
#         n = len(points)
#         for i in range(n):
#             x1, y1 = points[i]
#             for j in range(i + 1, n):
#                 x2, y2 = points[j]
#                 for k in range(j + 1, n):
#                     x3, y3 = points[k]
#                     curr = abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
#                     if curr > area:
#                         area = curr
#         return area
#
# #         dist = []
# #         for i in range(0 , len(points)):
# #             print (points[i])
#
# #             length = abs(points[i][0] - points[i][1])
# #             dist.append(length)
#
#
# #         print (dist)
# #         max1 = max(dist)
# #         dist.remove(max1)
# #         max2 = max(dist)
# #         area = 0.5 * max1 * max2
#
# #         print (area)
# #         return area
################ finding the maximum perimeter of triangle from given lengths in an array########### the tesla problem
#
# class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         nums.sort(reverse=True)
#
#         for i in range(3, len(nums) + 1):
#
#             if (nums[i - 3] < nums[i - 2] + nums[i - 1]):
#                 return sum(nums[i - 3:i])
#
#         return 0


##############finding senrior citizens from an encoded string####
# class Solution:
#     def countSeniors(self, details: List[str]) -> int:
#         age = []
#
#         for i in details:
#             age_num = i[11:13]
#             age.append(age_num)
#         count = 0
#
#         for i in age:
#             if i > '60':
#                 count += 1
#
#         print(count)
#
#         return count


########doing the baseball operations######
# class Solution:
#     def calPoints(self, operations: List[str]) -> int:

#         ans = []

#         for i in operations:
#             if i =='C':
#                 ans.pop()
#             elif i =='D':
#                 ans.append(ans[-1]*2)
#             elif i == '+':
#                 ans.append(ans[-1]+ ans[-2])
#             else:
#                 ans.append(int(i))

#         print(ans)
#         return sum(ans)


######min stack neetcode######
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.minStack = []
#
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if self.minStack:
#             self.minStack.append(min(val, self.minStack[-1]))
#         else:
#             self.minStack.append(val)
#
#     def pop(self) -> None:
#         self.stack.pop()
#         self.minStack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return self.minStack[-1]

############easy array problem#########
# class Solution:
#     def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
#         diff = []
#
#         for i in range(0, len(nums)):
#             prefix = nums[i + 1:]
#             print(prefix)
#             suffix = nums[:i + 1]
#             difference = len(set(suffix)) - len(set(prefix))
#             print(difference)
#
#             diff.append(difference)
#
#         return diff


############finding the row having max number of 1###########
# class Solution:
#     def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
#         n = len(mat)
#         m = len(mat[0])
#         row, count_one = 0, 0
#         for i in range(n):
#             one = 0
#             for j in range(m):
#                 if mat[i][j] == 1:
#                     one += 1
#
#             if one > count_one:
#                 count_one = one
#
#                 row = i
#
#         return [row, count_one]
#
#     #         ans = {}
# #         for i in mat:
# #             count = 0
# #             for j in i:
# #                 if j == 1:
# #                     count += 1
# #             ans[tuple(i)] = count
#
# #         print(ans)


########### finding number of occurences
# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         yolo = []
#         ans_set = set(arr)
#         print(ans_set)
#         for i in ans_set:
#             ans = arr.count(i)
#             yolo.append(ans)
#
#         yolo_set = set(yolo)
#
#         if len(yolo_set) == len(yolo):
#             return True
#         else:
#             return False


#####finding the strings within a range with vowels#######

# class Solution:
#     def vowelStrings(self, words: List[str], left: int, right: int) -> int:
#         vowel = ['a', 'e', 'i', 'o', 'u']
#         count = 0
#         for i in range(left, right + 1):
#             print(words[i][0])
#             print(words[i][-1])
#             if words[i][0] in vowel and words[i][-1] in vowel:
#                 count += 1
#                 print(count)
#
#         print(count)
#         return count


### two out of three###########
# class Solution:
#     def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
#         set_num1 = set(nums1)
#         set_num2 = set(nums2)
#         set_num3 = set(nums3)
#         ans = []
#
#         for i in set_num1:
#             ans.append(i)
#
#         for i in set_num2:
#             ans.append(i)
#
#         for i in set_num3:
#             ans.append(i)
#
#         set_ans = set(ans)
#
#         final_ans = []
#         for i in set_ans:
#             count = ans.count(i)
#             if count >= 2:
#                 final_ans.append(i)
#
#         print(final_ans)
#
#         return final_ans


###############removing the outer parentheses of valid parentheses###########
# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#
#         lCount, rCount = 0, 0
#         temp = []
#         ans = []
#         for char in s:
#             temp.append(char)
#             print(f"Temp while starting the for loop {temp}")
#             if char == '(':
#                 lCount += 1
#             elif char == ')':
#                 rCount += 1
#                 if lCount == rCount:
#                     ans += temp[1:-1]
#                     temp = []
#                     print(f"Ans in the if loop {ans}")
#
#         return ''.join(ans)



#########returning the discounted price of arrays depending on the condition#########

# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         ans = []
#         for i in range(0, len(prices)):
#             flag = False
#             for j in range(i + 1, len(prices)):
#                 if prices[i] >= prices[j]:
#                     ans.append(prices[i] - prices[j])
#                     flag = True
#                     break
#             if not flag:
#                 ans.append(prices[i])
#
#         print(ans)
#
#         return ans
#
########making the arrays in such a way that the sum is always 0######## microsoft asked question

# class Solution:
#     def sumZero(self, n: int) -> List[int]:
#         result = list(range(1, n))
#         print(result)
#         result.append(-(sum(result)))
#         print(result)
#         return result
######miost east string mnanipulation

# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#
#         if "".join(word1) == "".join(word2):
#             return True
#         else:
#             return False


######finding the  kth distinct element in an array #############
# class Solution:
#     def kthDistinct(self, arr: List[str], k: int) -> str:
#         ans = []
#         for i in arr:
#
#             if arr.count(i) == 1:
#                 print(i)
#                 ans.append(i)
#
#         if k <= len(ans):
#             return ans[k - 1]
#         else:
#             return ""

#returning the maximum sum of the minimum value in pairs of an array########
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         ans = []
#
#         for i in range(1, len(nums), 2):
#             ans.append(min(nums[i - 1], nums[i]))
#
#         return sum(ans)


######keep multiplying found values by 2######
# class Solution:
#     def findFinalValue(self, nums: List[int], original: int) -> int:
#
#         if original in nums:
#             while original in nums:
#                 original = original * 2
#
#         return original
###############lol################
#####returning if the array can be made into target array or not##########
# class Solution:
#     def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
#
#         if sorted(target) == sorted(arr):
#             return True
#         else:
#             return False


##############very important (traversing in a matrix########### lucky numbers
# class Solution:
#     def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
#
#         len_rows = len(matrix)
#         len_cols = len(matrix[0])
#         columns = []
#         for i in range(len_cols):
#             columns.append(0)
#         rows = set()
#         for i in range(len_rows):
#             rows.add(min(matrix[i]))
#         for i in range(len_rows):
#             for j in range(len_cols):
#                 columns[j] = max(columns[j], matrix[i][j])
#
#         ans = []
#         for i in columns:
#             if i in rows:
#                 ans.append(i)
#         return ans
################finding the difference between the arrays and targeted arrays########
# class Solution:
#     def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
#         count = 0
#         for i in arr1:
#             for j in arr2:
#                 if abs(i - j) <= d:
#                     break
#             else:
#                 count += 1
#
#         return count
#
# # class Solution:
# #     def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
#
#
# #         ans = []
#
# #         temp = 0
# #         for i in arr1:
# #             count = 0
# #             for j in arr2:
# #                 temp = abs(i - j)
# #                 if temp >=d:
# #                     count+=1
# #             if count == len(arr2):
# #                     print(i)
# #                     ans.append(count)
#
# #         print(ans)
#
# #         #return len(ans)
#
#######*************important problem - asked multiple times -- stack --************
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#
#         for op in tokens:
#             if op == '+':
#                 stack.append(stack.pop() + stack.pop())
#             elif op == '-':
#                 a = stack.pop()
#                 b = stack.pop()
#                 stack.append(b - a)
#             elif op == '*':
#                 stack.append(stack.pop() * stack.pop())
#             elif op == '/':
#                 a = stack.pop()
#                 b = stack.pop()
#                 stack.append(int(b / a))
#             else:
#                 stack.append(int(op))
#
#         return stack[0]

############maximum difference between tow elements########
# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#
#         ans = []
#
#         for i in range(0, len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] > nums[i]:
#                     max_diff = nums[j] - nums[i]
#                     ans.append(max_diff)
#
#         if len(ans) == 0:
#             return -1
#         else:
#             return max(ans)