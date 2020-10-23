# from typing import List
# class move:
#     def move_zero(self, nums: List):
#         if len(nums) <= 0:
#             raise IndexError("错误")
#         for j in range(len(nums) - 1):
#             for i in range(len(nums) - 1):
#                 if nums[i] == 0:
#                     nums[i], nums[i + 1] = nums[i + 1], nums[i]
#         return nums

from typing import List
# class move:
#     def move_zero(self,nums:List):
#         if len(nums)<=0 :
#             raise IndexError("错误")
#         for i in  range(len(nums),0):
#             slower=nums[i-1]
#             fast=nums[i-2]
#             while fast==0:

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         lists=nums
#         nums=[]
#         j=1
#         for i in lists:
#             if i not in nums:
#                 j+=1
#                 lists[j]=i
#         for i in nums:
#             if i in lists:

from typing import List








class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for j in range(len(nums)):
            for i in range(len(nums)-1):
                if nums[i]!=nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
        return  nums

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)

class link:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        cursor = self.head
        string = ""
        while cursor:
            string += "{}".format(cursor)
            cursor = cursor.next
        return string

    def remove(self,data:List):
        for i in  range(len(data)-1):
            data[i]=Node(data[i])
        self.size=len(data)
        self.head = data[0]
        self.tail = data[len(data)-1]
        cursor=self.head
        for i in range(len(data) - 1):
            if data[i] !=self.tail:
                cursor.next=data[i+1]
                cursor=cursor.next

        while cursor.next==cursor:
            cursor.next=cursor.next.next
            cursor = cursor.next
        return data



        # for j in range(1,len(nums)):
        #             if nums[j]!=nums[j-1]:
        #                 print(nums[j-1])
        print(nums[len(nums)-1])


li=Solution()
data=li.removeDuplicates([1,1,2,4,4,4,2,1,2,3,9])
lim=link()
print(lim.remove(data))



