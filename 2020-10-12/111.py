# def sums():
#     result = 0
#     for i in range(100000000):
#         result +=i
#     return result
# import time
# start = time.time()
# sums()
# end = time.time()
# print(f'用时{end-start}')
from typing import  List
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []
#         for i in range (len(nums)-2):
#             if i > 0 and nums[i-1] == nums[i]:
#                 continue
#             left = i + 1
#             right = len(nums) - 1
#             while left < right:
#                 if nums[i] + nums[left] + nums[right] > 0:
#                     right -= 1
#                 elif nums[i] + nums[left] + nums[right] < 0 :
#                     left += 1
#                 else:
#                     res.append([nums[i],nums[left],nums[right]])
#
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1
#                     left += 1
#                     right -= 1
#         return res