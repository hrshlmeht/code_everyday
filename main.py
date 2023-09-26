#####merging the sorted array in the same#####
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


########rearrange the array without deleting the numbers######
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