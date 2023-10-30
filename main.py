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

########gneerating the paranthesis of given integer using back tracking #####################
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#
#         stack = []
#         result = []
#
#         def back_tracking(count_closed, count_open):
#
#             if count_closed == count_open == n:
#                 result.append("".join(stack))
#                 return
#
#             if count_open < n:
#                 stack.append('(')
#                 back_tracking(count_closed, count_open + 1)
#                 stack.pop()
#
#             if count_closed < count_open:
#                 stack.append(')')
#                 back_tracking(count_closed + 1, count_open)
#                 stack.pop()
#
#         back_tracking(0, 0)
#         return result


#############fuzzbuzz asked in ericsson (from leetcode)############
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         ans = []
#         for i in range(1, n + 1):
#             if i % 3 == 0 and i % 5 == 0:
#                 ans.append("FizzBuzz")
#             elif i % 3 == 0:
#                 ans.append("Fizz")
#             elif i % 5 == 0:
#                 ans.append("Buzz")
#             else:
#                 ans.append(str(i))
#
#         print(ans)
#         return (ans)


###############daily temperatures neetcode##########

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = [0] * len(temperatures)
#         stack = []  # pair: value, index
#         for i, t in enumerate(temperatures):
#             # if the next elem is greater than current element
#             while stack and t > stack[-1][0]:  # [-1]= top,[0]= 1st elem
#                 stackT, stackInd = stack.pop()
#                 res[stackInd] = (i - stackInd)
#             stack.append([t, i])
#
#         print(stack)
#         print(res)
#     # return res


#########easy and treat leetcode problem#########
# class Solution:
#     def targetIndices(self, nums: List[int], target: int) -> List[int]:
#
#         nums = sorted(nums)
#         ans = []
#         for i in range(0, len(nums)):
#             if nums[i] == target:
#                 ans.append(i)
#
#         print(ans)
#         return ans


####Merge the tools problem from hacker_rank###########

# def merge_the_tools(string, k):
#     # your code goes here
#     ans = []
#     j = 0
#     for i in range(0, len(string), k):
#         ans.append(string[i:(i + k)])
#
#     for i in ans:
#         s = ""
#         for j in i:
#             if j not in s:
#                 s += j
#         print(s)
#
#
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)


###returning the maximum value of a string in an array#########
# class Solution:
#     def maximumValue(self, strs: List[str]) -> int:
#         ans = []
#         for i in range(0, len(strs)):
#             if strs[i].isnumeric():
#                 ans.append(int(strs[i]))
#             elif strs[i].isdigit():
#                 ans.append(len(strs[i]))
#             else:
#                 ans.append(len(strs[i]))
#
#         print(ans)
#         return max(ans)


####maximum subarray##########

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#
#         if len(nums) == 0:
#             return nums[0]
#
#         ans = nums[0]
#         marker = nums[0]
#
#         for i in range(1, len(nums)):
#             current = max(nums[i], nums[i] + marker)
#             ans = max(ans, current)
#             marker = current
#
#         print(ans)
#         return ans
#
# #         ans = []
# #         sum_ans = []
# #         for i in nums:
# #             ans.append(i)
# #             j = sum(ans)
# #             sum_ans.append(j)
#
# #         print(ans)
# #         print(sum_ans)


#####finding the GCD of max and min in an array####
#
# class Solution:
#     def findGCD(self, nums: List[int]) -> int:
#
#         minimum = min(nums)
#         maximum = max(nums)
#         ans = []
#         for i in range(1, maximum + 1):
#             if maximum % i == 0 and minimum % i == 0:
#                 ans.append(i)
#
#         print(ans)
#         if len(ans) == 0:
#             return 1
#         else:
#             return max(ans)

####maximum product difference between two pairs######
# class Solution:
#     def maxProductDifference(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#
#         min_pair_prod = nums[0] * nums[1]
#
#         max_pair_prod = nums[len(nums) - 1] * nums[len(nums) - 2]
#
#         return max_pair_prod - min_pair_prod


#######Smaleest index with equal value#####
# class Solution:
#     def smallestEqual(self, nums: List[int]) -> int:
#
#         for i in range(0, len(nums)):
#             if i % 10 == nums[i]:
#                 return i
#
#         return -1


######range sum of sorted subarray sums#####
# class Solution:
#     def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
#         sum_ans = []
#         for i in range(0, len(nums)):
#             arr = 0
#             for j in range(i, len(nums)):
#                 arr += nums[j]
#                 sum_ans.append(arr)
#
#         print(sum_ans)
#         sum_ans = sorted(sum_ans)[left - 1:right:]
#         return sum(sum_ans) % 1000000007


#######lol - checking the anagram using inbuilt functions########

# class Solution:
#     def checkIfPangram(self, sentence: str) -> bool:
#         set_len = set(sentence)
#
#         if len(set_len) == 26:
#             return True
#
#         return False

#########number of string that appear a sa substring word###

# class Solution:
#     def numOfStrings(self, patterns: List[str], word: str) -> int:
#
#         count = 0
#
#         for i in patterns:
#             if i in word:
#                 count += 1
#
#         print(count)
#
#         return (count)



#reverse vowels of a string using 2 pointers#######

# class Solution:
#     def reverseVowels(self, s: str) -> str:
#
#         list_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
#         i = 0
#         j = len(s) - 1
#         s = list(s)
#         while i < j:
#             if s[i] not in list_vowels:
#                 i += 1
#             if s[j] not in list_vowels:
#                 j -= 1
#             if s[i] in list_vowels and s[j] in list_vowels:
#                 s[i], s[j] = s[j], s[i]
#                 i += 1
#                 j -= 1
#         s = "".join(s)
#         print(s)
#         return s


#############reversing the integer######
# class Solution:
#     def reverse(self, x: int) -> int:
#         negative = x < 0
#         x = str(abs(x))
#         ans_int = int(x[::-1])
#
#         if negative:
#             ans_int *= -1
#
#         if ans_int < -2 ** 31 or ans_int > 2 ** 31 - 1:
#             return 0
#
#         return ans_int


###############minimum steps to reach 0######

# class Solution:
#     def numberOfSteps(self, num: int) -> int:
#
#         count = 0
#
#         while num > 0:
#             if num % 2 == 0:
#                 num = num // 2
#                 count += 1
#                 # print(count)
#             else:
#                 num = num - 1
#                 count += 1
#
#         print(count)
#         return count


#########################################

# class Solution:
#     def minSubarray(self, nums: List[int], p: int) -> int:
#
#         sum_array = sum(nums)
#
#         if sum_array % p == 0:
#             return 0
#
#         ans = []
#         for i in nums:
#
#             print(i)
#             print(sum_array)
#             if (sum_array - i) % p == 0:
#                 ans.append(i)
#                 sum_array = sum_array - i
#
#         print(ans)
#         return len(ans)

########checking if the array is monolithic or not########
# class Solution:
#     def isMonotonic(self, nums: List[int]) -> bool:
#         nums_sorted = sorted(nums)
#
#         if nums == nums_sorted or nums == nums_sorted[::-1]:
#             return True
#
#         return False

########maximum number of enemy forts that can be captured####
#
# class Solution:
#     def captureForts(self, forts: List[int]) -> int:
#         if 1 not in forts and -1 not in forts: return 0
#         output_forward = []
#         count = 0
#         flag = False
#         for i in forts:
#             if i == 1:
#                 flag = True
#                 count = 0
#
#             elif i == -1:
#                 flag = False
#                 output_forward.append(count)
#
#             if flag and i == 0:
#                 count += 1
#                 # output_forward.append(count)
#
#         print(output_forward)
#
#         output_backward = []
#         count_back = 0
#         flag = False
#         for i in range(len(forts) - 1, -1, -1):
#             if forts[i] == 1:
#                 flag = True
#                 count_back = 0
#
#             elif forts[i] == -1:
#                 flag = False
#                 output_backward.append(count_back)
#
#             if flag == True and forts[i] == 0:
#                 count_back += 1
#                 # output_backward.append(count_back)
#
#         print(output_backward)
#         output_forward += output_backward
#         if len(output_forward) == 0:
#             return 0
#
#         else:
#             return max(output_forward)
#
#
#
#
##########reversing the string##########
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         left  , right = 0 , len(s)-1
#
#         while left < right:
#             s[left], s[right] = s[right] , s[left]
#             left +=1
#             right -=1


#########minimum cost required to move to strings#####
# class Solution:
#     def minCostToMoveChips(self, position: List[int]) -> int:
#         even, odd = 0, 0
#         n = len(position)
#         for i in position:
#             if i % 2 == 0:
#                 even += 1
#             else:
#                 odd += 1
#         if even == n or odd == n:
#             return 0
#         else:
#             return min(even, odd)

#########Number of arithmetic triplets######
# class Solution:
#     def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
#         result = 0
#         for i in range(0, len(nums)):
#             if nums[i] + diff in nums and nums[i] + (diff * 2) in nums:
#                 result += 1
#
#         print(result)
#         return result
#

##########Excel sheet column title#########
# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         result = ""
#         while columnNumber > 0:
#             columnNumber -= 1
#             result = chr(columnNumber % 26 + ord('A')) + result
#             columnNumber //= 26
#
#         print(result)
#         return result

#######Excel sheet column number########
# class Solution:
#     def titleToNumber(self, columnTitle: str) -> int:
#
#         answer = 0
#         for i in columnTitle:
#             answer = answer * 26 + (ord(i)- ord('A')+ 1)
#
#         print(answer)
#         return answer


########ceells in a range of excel sheet###########
# class Solution:
#     def cellsInRange(self, s: str) -> List[str]:
#
#         ans = []
#
#         numeric_start = int(s[1:2])
#         print(numeric_start)
#         numeric_end = int(s[4:5])
#         print(numeric_end)
#         character_start_num = ord(s[0:1])
#         print(character_start_num)
#         character_end_num = ord(s[3:4])
#         print(character_end_num)
#
#         for i in range(character_start_num, character_end_num + 1):
#             ans_string = ''
#             for j in range(numeric_start, numeric_end + 1):
#                 ans_string = chr(i) + str(j)
#                 ans.append(ans_string)
#
#         print(ans)

########sort array by parity#######
# class Solution:
#     def sortArrayByParityII(self, nums: List[int]) -> List[int]:
#         even = []
#         odd = []
#         lst=[]
#         for i in range(len(nums)):
#             if nums[i]%2 == 0:
#                 even.append(nums[i])
#             else:
#                 odd.append(nums[i])
#         for i in range(len(even)):
#             lst.append(even[i])
#             lst.append(odd[i])
#         return lst


############3 sum####
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#
#         nums = sorted(nums)
#         triplet = set()
#         for i in range(0, len(nums) - 2):
#             first_num = nums[i]
#             j = i + 1
#             k = len(nums) - 1
#             while j < k:
#                 second_num = nums[j]
#                 third_num = nums[k]
#                 potential_sum = first_num + second_num + third_num
#                 if potential_sum > 0:
#                     k -= 1
#                 elif potential_sum < 0:
#                     j += 1
#                 else:
#                     triplet.add((first_num, second_num, third_num))
#                     j += 1
#                     k -= 1
#
#         return triplet


####################length of the longest substring##############
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#
#         len_sub = []
#
#         prev = ""
#
#         i = 0
#         while i < len(s):
#             j = i
#             cnt = 0
#             while (j < len(s) and s[j] not in prev):
#                 prev = prev + s[j]
#                 cnt += 1
#                 j += 1
#             prev = ""
#             i += 1
#             len_sub.append(cnt)
#         print(len_sub)
#         if len(len_sub) == 0:
#             return 0
#
#         return max(len_sub)
#


##########sort arrays by parity########
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#
#         ans_even = []
#         ans_odd = []
#         ans_final = []
#         for i in nums:
#             if i % 2 == 0:
#                 ans_even.append(i)
#             else:
#                 ans_odd.append(i)
#
#         print(ans_odd)
#         print(ans_even)
#
#         for i in range(0, len(ans_even)):
#             ans_final.append(ans_even[i])
#
#         for i in range(0, len(ans_odd)):
#             ans_final.append(ans_odd[i])
#
#         print(ans_final)
#
#         return ans_final

#################word break##########
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [False] * (len(s) + 1)
#         dp[len(s)] = True
#
#         for i in range(len(s) - 1, -1, -1):
#
#             for w in wordDict:
#
#                 if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
#                     dp[i] = dp[i + len(w)]
#                 if dp[i]:
#                     break
#
#         return dp[0]


###########toeplitiz matrix##########
# class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         for i in range(0, len(matrix) - 1):
#
#             for j in range(0, len(matrix[i]) - 1):
#
#                 if matrix[i][j] != matrix[i + 1][j + 1]:
#                     return False
#
#         return True
#


##########good triplets brute force method##########
# class Solution:
#     def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
#
#         answer = 0
#         for i in range(len(arr) - 2):
#             for j in range(len(arr) - 1):
#                 for k in range(len(arr)):
#                     if i >= 0 and i < j and j < k and k < len(arr):
#                         if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
#                             answer += 1
#
#         return answer


########defanging an IP address#
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#
#         ans_str = ''
#
#         for i in address:
#             if i == '.':
#                 ans_str += '[.]'
#             else:
#                 ans_str += i
#
#         print(ans_str)
#         return ans_str

###########Ransom Note########
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#
#         for i in ransomNote:
#             if i in magazine:
#                 magazine = magazine.replace(i, "", 1)
#             else:
#                 return False
#
#         return True
#
#         # #magzine_set = set(magazine)
#         # ans = False
#         # for i in ransomNote:
#         #     if i not in magazine:
#         #         return False
#
#         # return True


######checking the jewels and stones#######
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         count = 0
#         for i in stones:
#             if i in jewels:
#                 count += 1
#
#         print(count)
#         return count


####reversing the string 3########### common interview question
# def reverseWords(self, s: str) -> str:
#     ans = []
#     s = s + ' '
#     ans_string = ''
#     for i in s:
#         # print(i)
#         if i == ' ':
#             ans.append(ans_string)
#             ans_string = ''
#         else:
#             ans_string = ans_string + i
#
#     print(ans)
#     final_ans = ''
#     for i in ans:
#         final_ans = final_ans + ' ' + i[::-1]
#
#     final_ans = final_ans.strip()
#     return final_ans
# class Solution:
#

#########leetcode strings######
# class Solution:
#     def interpret(self, command: str) -> str:
#         command = command.replace('()', 'o')
#         command = command.replace('(al)', 'al')
#         return command

#
# class Solution:
#     def diStringMatch(self, s: str) -> List[int]:
#
#         ans = []
#
#         lower = 0
#         upper = len(s)
#
#         for i in s:
#             if i == 'I':
#                 ans.append(lower)
#                 lower += 1
#             else:
#                 ans.append(upper)
#                 upper -= 1
#
#         if s[len(s) - 1] == 'I':
#             ans.append(upper)
#         else:
#             ans.append(lower)
#
#         return ans

#######leetcode solution for = relative sort array##########
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         count = [0] * 1001
#
#         for num in arr1:
#             count[num] += 1
#         result = []
#         for num in arr2:
#             result.extend([num] * count[num])
#             count[num] = 0
#         for i in range(1001):
#             if count[i] > 0:
#                 result.extend([i] * count[i])
#         return result


#############leetcode strictly increasing###################
# class Solution:
#     def validMountainArray(self, arr: List[int]) -> bool:
#         strictly_increasing = False
#         strictly_decreasing = False
#
#         for i in range(1, len(arr)):
#             if arr[i] > arr[i - 1]:
#                 if strictly_decreasing:
#                     return False
#                 strictly_increasing = True
#             elif arr[i] < arr[i - 1]:
#                 if not strictly_increasing:
#                     return False
#                 strictly_decreasing = True
#             else:
#                 return False
#
#         return True if strictly_increasing and strictly_decreasing else False


#######count number of pairs whose sum is less than target###########
# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         return sum(
#             nums[i] + nums[j] < target
#             for i in range(len(nums))
#             for j in range(i + 1, len(nums))
#


##########leetcode hard##### =median of the sorted arrays##########
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums1.extend(nums2)  # Combine the arrays
#
#         sorted_arr = sorted(nums1)  # Sort the combined array
#
#         n = len(sorted_arr)
#         if n % 2 == 0:
#             m1 = sorted_arr[n // 2 - 1]
#             m2 = sorted_arr[n // 2]
#             return (m1 + m2) / 2
#         else:
#             return sorted_arr[n // 2]


#########leetcode wiggle subsequecne########
# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#
#         inc = 1
#         dec = 1
#
#         for i in range(1, len(nums)):
#             if nums[i] > nums[i - 1]:
#                 inc = dec + 1
#             elif nums[i] < nums[i - 1]:
#                 dec = inc + 1
#
#         return max(inc, dec)


##leetcode problem - contactenating the array and returning the sum of them#########
# class Solution:
#     def findTheArrayConcVal(self, nums: List[int]) -> int:
#         j = len(nums) - 1
#         ans = 0
#
#         for i in range(len(nums)):
#             if i == j:
#                 ans += nums[i]
#                 break
#
#             ans_str = str(nums[i]) + str(nums[j])
#             ans += int(ans_str)
#             j = j - 1
#
#             if i >= j:
#                 break
#
#         return ans


## 3 sum closest######
# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         closet = float('inf')
#         nums.sort()
#         for i in range(len(nums) - 2):
#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 sum3 = nums[i] + nums[l] + nums[r]
#                 print(sum3)
#                 if sum3 < target:
#                     l += 1
#                 else:
#                     r -=1
#                 if abs(sum3 - target) < abs(closet - target):
#                     closet = sum3
#         return closet


###########is acronym##########
# class Solution:
#     def isAcronym(self, words: List[str], s: str) -> bool:
#         ans = ''
#         for i in words:
#             ans = ans + i[0]
#
#         if ans == s:
#             return True
#
#         return False

### check if it is possible to split the array or not ## leetcode medium###
# class Solution:
#     def canSplitArray(self, nums: List[int], m: int) -> bool:
#
#         if len(nums) < 3:
#             return True
#
#         for i in range(len(nums) - 1):
#             if nums[i] + nums[i + 1] >= m:
#                 return True
#
#         return False



###buying two chocolates##############


# class Solution:
#     def buyChoco(self, prices: List[int], money: int) -> int:
#
#         prices = sorted(prices)
#         print(prices)
#         for i in range(1 , len(prices)):
#             if prices[i] + prices[i-1] <= money:
#                 return money - (prices[i] + prices[i-1])
#             else:
#                 return money
#

##rotating the array
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         new_lis = matrix.copy()
#         matrix.clear()
#
#         for _ in range(len(new_lis)):
#             matrix.append([])
#         for i in range(len(new_lis)):
#             for j in range(len(new_lis[0])):
#                 # print(l[j][0])
#                 div_ = j % len(new_lis[0])
#                 matrix[j].insert(0, new_lis[i][div_])
#
#
#         return(matrix)

###house robber2##########
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         memo = [-1 for _ in range(len(nums))]
#
#         def dp(i):
#             if i < 0: ac
#             return 0
#             a
#
#         elif memo[i] >= 0:
#         return memo[i]
#
#     else:
#     res = max(dp(i - 2) + nums[i], dp(i - 1))
#     memo[i] = res
#     return res
#
#
# a = dp(len(nums) - 2)
# memo = [-1 for _ in range(len(nums))]
# nums.pop(0)
# b = dp(len(nums) - 1)
# return max(a, b)
# # class Solution:
# #     def rob(self, nums: List[int]) -> int:
#
# #         ans_even = []
# #         ans_odd = []
#
# #         for i in range ( 0 , len(nums)):
#
# #             print(i)
#
# #             if i == 0 or i % 2 == 0:
# #                 ans_even.append(nums[i])
# #             else:
# #                 ans_odd.append(nums[i])
#
#
# #         print (ans_even)
# #         print (ans_odd)
# #         ans1 = sum(ans_even)
# #         ans2 = sum(ans_odd)
#
# #         return max(ans1 , ans2)
#
#


#######minimun sum index of 2 lists######
# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         res = len(list1) + len(list2)
#         ans = {}
#         x = []
#         for word in list1:
#             if word == " ":
#                 continue
#             if word in list2:
#                 ln = list1.index(word) + list2.index(word)
#                 res = min(res, ln)
#                 ans[word] = ln
#
#         for key, val in ans.items():
#             if val == res:
#                 x.append(key)
#
#         return x

#######adding the 2d arrays###########
# class Solution:
#     def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
#         merged = []
#         ptr1, ptr2 = 0, 0
#
#         while ptr1 < len(nums1) or ptr2 < len(nums2):
#             id1 = nums1[ptr1][0] if ptr1 < len(nums1) else float('inf')
#             id2 = nums2[ptr2][0] if ptr2 < len(nums2) else float('inf')
#
#             if id1 < id2:
#                 merged.append(nums1[ptr1])
#                 ptr1 += 1
#             elif id1 > id2:
#                 merged.append(nums2[ptr2])
#                 ptr2 += 1
#             else:
#                 merged.append([id1, nums1[ptr1][1] + nums2[ptr2][1]])
#                 ptr1 += 1
#                 ptr2 += 1
#
#         return merged
#
# # class Solution:
# #     def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
# #         index_list = []
# #         index_list_1 = []
# #         index_list_2 = []
#
# #         for i in nums1:
# #             index_list_1.append(i[0])
# #             index_list.append(i[0])
#
# #         for j in nums2:
# #             index_list_2.append(j[0])
# #             index_list.append(j[0])
#
# #         set_list = set(index_list)
# #         print(index_list_1)
# #         print(index_list_2)
#
# #         print(set_list)
# #         ans_final = []
# #         for i in set_list:
# #             if i in index_list_1 and i not in index_list_2:
# #                 print(i)
# #                 # Append the corresponding element from nums1
# #                 ans_final.append(nums1[index_list_1.index(i)])
# #             elif i in index_list_2 and i not in index_list_1:
# #                 # Append the corresponding element from nums2
# #                 ans_final.append(nums2[index_list_2.index(i)])
# #             else :
# #                 # Append the corresponding elements from both nums1 and nums2
# #                 ans_final.append([nums1[index_list_1.index(i)], nums2[index_list_2.index(i)]])
#
# #         print(ans_final)

## merge the arrays in a single one
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         tot = len(nums1)-1
#         for i in range(len(nums2)-1,-1,-1):
#             while m>0 and nums2[i]< nums1[m-1]:
#                 nums1[tot] = nums1[m-1]
#                 tot-=1
#                 m-=1
#             nums1[tot] = nums2[i]
#             tot-=1


#########array problem with replacing the rearranging depending upon the values###
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         j = 0
#
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 nums[i] = None
#             else:
#                 if nums[j] == None:
#                     nums[j], nums[i] = nums[i], nums[j]
#
#                 j += 1
#
#         return j
#         print(nums)

######remove duplicates in the array
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         j = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[j] = nums[i]
#                 j += 1
#         return j

#########reverse the string 3##########
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         ans = []
#         s = s + ' '
#         ans_string = ''
#         for i in s:
#             # print(i)
#             if i == ' ':
#                 ans.append(ans_string)
#                 ans_string = ''
#             else:
#                 ans_string = ans_string + i
#
#         print(ans)
#         final_ans = ''
#         for i in ans:
#             final_ans = final_ans + ' ' + i[::-1]
#
#         final_ans = final_ans.strip()
#         print(final_ans)
#         return final_ans
#
#
#
###########remove duplicates from a sorted array##########
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if len(nums) <= 2:
#             return len(nums)
#
#         currentIndex = 2
#         for i in range(2, len(nums)):
#             if nums[i] != nums[currentIndex - 2]:
#                 nums[currentIndex] = nums[i]
#                 currentIndex += 1
#
#         return currentIndex

###rotate the array as per user input (without changing the size of the array#########
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             a = nums.pop()
#             nums.insert(0 ,a)


######best time to buy and sell the stock######
# class Solution(object):
#     def maxProfit(self, prices):
#
#         if len(prices) == 0:
#             return 0
#
#         left = 0
#         right = 1
#         max_profit = 0
#
#         while right < len(prices):
#             if prices[left] < prices[right]:
#                 profit = prices[right] - prices[left]
#                 max_profit = max(profit, max_profit)
#             else:
#                 left = right
#             right += 1
#
#         print(max_profit)
#         return max_profit
#
#


####leetcode problem = Letter combination of a phone number
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#
#         main_dic = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }
#
#         if not digits:
#             return []
#
#         if len(digits) == 1:
#             return list(main_dic[digits])
#
#         current_combinations = list(main_dic[digits[0]])
#         next_combinations = self.letterCombinations(digits[1:])
#
#         ans = []
#         for c in current_combinations:
#             for n in next_combinations:
#                 ans.append(c + n)
#
#         return ans


########running the encoded string#######
# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         result = []
#         for i in range(0, len(nums), 2):
#             freq = nums[i]
#             val = nums[i + 1]
#             result.extend([val] * freq)
#
#         print(result)
#         return result

#####finding the closest distance to zero fromn the given array#########
# class Solution:
#     def findClosestNumber(self, nums: List[int]) -> int:
#         closest_num = nums[0]
#         min_diff = abs(nums[0] - 0)
#
#         for i in nums[1:]:
#             j1 = abs(i)
#             if j1 < min_diff:
#                 min_diff = j1
#                 closest_num = i
#             elif j1 == min_diff and i > closest_num:
#                 closest_num = i
#
#         return closest_num
