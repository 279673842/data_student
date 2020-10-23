# nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
# nums[1:len(nums) - 1] = nums[2:]
# print(nums)
# nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
# nums[1:] = nums[2:]
# print(nums)
#
#
# #
# # from    typing import List
# # class Solution:
# #     def removeDuplicates(self, nums: List[int]) -> int:
# #         n=len(set(nums))
# #         i=0
# #         while i<n:
# #             if nums[i]==nums[i+1]:
# #                 temp=nums[i]
# #                 nums[i+1:len(nums)-1]=nums[i+2:]
# #                 nums[-1] = temp
# #             else:
# #                 i+=1
#
# #
# #
# #
# #
# # from    typing import List
# # class Solution2:
# #     def removeDuplicates(self, nums: List[int]) -> int:
# #         slow=0
# #         fast=1
# #         while fast<len(nums):
# #             if nums[slow]==nums[fast]:
# #                 fast+=1
# #             else:
# #                 slow+=1
# #                 nums[slow] = nums[fast]
# #                 fast+=1
# #
# #         return slow+1
#
#
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         fast = 0
#         slow = 0
#         while fast < len(nums):
#             if nums[fast] == 0:
# #                 fast += 1
# #             else:
# #                 nums[slow] = nums[fast]
# #                 slow += 1
# #                 fast += 1
# #         for i in range(slow, len(nums)):
# #             nums[i] = 0
# #             # nums.pop
# #
# # from typing import  List
# # class Solution:
# #     def removeElement(self, nums: List[int], val: int) -> int:
# #         fast=0
# #         slow=0
# #         while fast<len(nums):
# #             if nums[fast]==val:
# #                 fast+=1
# #             else:
# #                 nums[slow]=nums[fast]
# #                 fast += 1
# #                 slow+=1
# #         return slow
# # li=Solution()
# # print(li.removeElement([0,1,2,2,3,0,4,2],2))
# # from typing import  List
# # class Solution:
# #     def removeDuplicates(self, nums: List[int]) -> int:
# #         fast=1
# #         slow=0
# #         while fast=
#
#
# from typing import  List
# class Solution2:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         fast=1
#         slow=0
#         count=1
#         while fast< len(nums):
#             if nums[slow]==nums[fast]:
#                 count+=1
#                 if count==2:
#                     slow+=1
#                     nums[slow]=nums[fast]
#                 fast+=1
#             else:
#                 slow+=1
#                 nums[slow] = nums[fast]
#                 count=1
#                 fast+=1
#         return slow+1
#
#
#
#














# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#     def __repr__(self):
#         return "Node({})".format(self.data)
# class link:
#     def __init__(self):
#         self.head=None
#         self.size=0
#
#     def remove(self,data):
#         node=Node(data)
#         if self.head:
#             curcor=self.head
#             for i in range(self.size):
#                 if self.head==node:
#                     self.head.next=None
#                 elif curcor.next==node :
#                     curcor.next=curcor.next.next
#                 else:
#                     curcor=curcor.next
#
#         else:
#             raise IndexError("空")
#
#
# li=link()
# li.remove(1)
# print(li)
#




class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)
class link:
    def __init__(self):
        self.head=None
        self.size=0














