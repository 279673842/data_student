# from typing import List
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         # nums1=nums1[:m]
#         # nums1.extend(nums2)
#         # nums1.sort()
#         j=0
#         for i in nums2:
#             nums1[m+j]=i
#             j+=1
#         nums1.sort()
#         return nums1
#
#
# q=Solution()
# print(q.merge([1,2,3,0,0,0],3,[2,5,6],3))
#
# # mid = int(len(nums) / 2)
# # head = 0
# # end = len(nums) - 1
# # while head < mid and mid < end:
# #     if nums[head] + nums[end] + nums[mid] == 0:
# #         b = [head, end, mid]
# #     elif nums[head] + nums[end] + nums[mid] > 0:
# #         end -= 1
# #         if nums[head] + nums[end] + nums[mid] == 0:
# #             b = [head, end, mid]
# #         elif nums[head] + nums[end] + nums[mid] > 0:
# #             end -= 1
# #         elif nums[head] + nums[end] + nums[mid] < 0:
# #             end += 1
# #             mid -= 1
# #     elif nums[head] + nums[end] + nums[mid] < 0:
# #         head += 1
# #         if nums[head] + nums[end] + nums[mid] == 0:
# #             b = [head, end, mid]
# #         elif nums[head] + nums[end] + nums[mid] > 0:
# #             head -= 1
# #             mid -= 1
# #         elif nums[head] + nums[end] + nums[mid] < 0:
# #             head += 1
# # class Solution:
# #     def threeSum(self, nums: List[int]) -> List[List[int]]:
# #         nums.sort()
#         # a=[]
#         # for i in range(len(nums)):
#         #     for j in range(i+1,len(nums)):
#         #         for k in nums[j+1:]:
#         #             if nums[i]+nums[j]+k==0:
#         #                 b=[nums[i],nums[j],k]
#         #                 while b not in a:
#         #                     a.append(b)
#
#         #                     a.append(b)
#
#         # return a
#
#
# class Solution2:
#     def threeSum(self, nums: [int]) -> [[int]]:
#         nums.sort()
#         res, k = [], 0
#         for k in range(len(nums) - 2):
#             if nums[k] > 0: break  # 1. because of j > i > k.
#             if k > 0 and nums[k] == nums[k - 1]: continue  # 2. skip the same `nums[k]`.
#             i, j = k + 1, len(nums) - 1
#             while i < j:  # 3. double pointer
#                 s = nums[k] + nums[i] + nums[j]
#                 if s < 0:
#                     i += 1
#                     while i < j and nums[i] == nums[i - 1]:
#                         i += 1
#                 elif s > 0:
#                     j -= 1
#                     while i < j and nums[j] == nums[j + 1]:
#                         j -= 1
#                 else:
#                     res.append([nums[k], nums[i], nums[j]])
#                     i += 1
#                     j -= 1
#                     while i < j and nums[i] == nums[i - 1]:
#                         i += 1
#                     while i < j and nums[j] == nums[j + 1]:
#                         j -= 1
#         return res
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res=[]
#         head = 0
#         for head in range(len(nums)-2):
#             if nums[head]>0:
#                 break
#             if head > 0 and nums[head] == nums[head-1]:
#                 continue
#             mid = head+1
#             end = len(nums) - 1
#             while mid< end:
#                 result=nums[head] + nums[end] + nums[mid]
#                 if result == 0:
#                     res.append([nums[head] , nums[mid], nums[end] ])
#                     mid+=1
#                     end -= 1
#                     while mid < end and nums[mid] == nums[mid - 1]:
#                         mid+=1
#                     while mid < end and nums[end] == nums[end+1]:
#                         end-=1
#                 elif result < 0:
#                     mid += 1
#                     while mid < end and nums[mid] == nums[mid - 1]:
#                         mid+=1
#
#                 elif result > 0:
#                     end-=1
#                     while mid < end and nums[end] == nums[end+1]:
#                         end-=1
#                 # res.append(b)
#         return res
# s=Solution()
# print(s.threeSum([1,-1,-1,0]))
# s=Solution2()
# print(s.threeSum([1,-1,-1,0]))

# def index(nums,data):
#     curr=int(len(nums)/2)
#     mid=nums[curr]
#     if data > mid:
from typing import List
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         curr=0
#         # mid=nums[curr]
#         while True:
#             if target > nums[curr]:
#                 curr+=1
#             elif target < nums[curr]:
#                 curr-=1
#             elif target == nums[curr]:
#                 return curr
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # j=0
        # for i in nums2:
        #     nums1[m+j]=i
        #     j+=1
        # nums1.sort()
        j=0
        i=0
        s=0
        if m==0 and n==1:
            nums1[0]=nums2[0]
        elif  m==0 and n!=0:
            nums1=nums2
        while i < m and j<n and s< len(nums1) :


            if nums1[m-1-i] <nums2[n-1-j]:
                nums1[len(nums1)-1-s]=nums2[n-1-j]

                j+=1
            elif nums1[m-1-i] >nums2[n-1-j]:
                nums1[len(nums1)-1-s]=nums1[m-1-i]
                nums1[m - 1 - i]=0
                if m-1-i !=0:
                    i+=1
            elif  nums1[m-1-i] ==nums2[n-1-j]:
                nums1[len(nums1)-1-s]=nums2[n-1-j]
                j+=1
            s+=1
        return nums1
li=Solution()
print(li.merge([0,0,0,0,0],0, [1,2,3,4,5],5))
# 负数


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # j=0
        # for i in nums2:
        #     nums1[m+j]=i
        #     j+=1
        # nums1.sort()
        i = m - 1
        j = n - 1
        s = m+n-1
        # if m == 0 and n == 1:
        #     nums1[0] = nums2[0]
        # elif m == 0 and n != 0:
        #     for i in nums2:
        #         nums1[m + j] = i
        #         j += 1
        while i >0 and j >0 and s >0:
            if nums1[m - 1 - i] < nums2[n - 1 - j]:
                nums1[len(nums1) - 1 - s] = nums2[n - 1 - j]
                j += 1
            elif nums1[m - 1 - i] > nums2[n - 1 - j]:
                nums1[len(nums1) - 1 - s] = nums1[m - 1 - i]
                nums1[m - 1 - i] = 0
                if m - 1 - i != 0:
                    i += 1
            elif nums1[m - 1 - i] == nums2[n - 1 - j]:
                nums1[len(nums1) - 1 - s] = nums2[n - 1 - j]
                j += 1
            s += 1
            while n - 1 - j >= 0:
                nums1[len(nums1) - 1 - s] = nums2[n - 1 - j]
                j -= 1
        return nums1
