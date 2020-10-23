"""
Author:BAI先生
github:主页NONE
"""
class Aeeay:
    def __init__(self,capacity=2):
        self.array=[None]*capacity
        self.size=0

    def invert(self,index,element):
        if index<0 or index>self.size:
            raise IndexError(" 超限")
        if index>=len(self.array) or self.size>=len(self.array):
            self.addcapacity()
        for i in range(self.size-1,index-1,-1):
            self.array[i+1]=self.array[i]
        self.array[index]=element
        self.size+=1

    def remove(self,index):
        if index<0 or index>self.size:
            raise IndexError(" 超限")
        if self.size>=len(self.array):
            self.addcapacity()
        for i in range(index,self.size):
            self.array[i]=self.array[i+1]
        self.size -= 1

    def addcapacity(self):
        new_array=[None]*(len(self.array)+1)
        for i in range(len(self.array)):
            new_array[i]=self.array[i]
        self.array=new_array
    def output(self):
        for i in range (self.size):
            print(self.array[i])

li=Aeeay()
li.invert(0,5)
print(li)
li.invert(0,6)
print(li)
li.remove(0)
print(li)


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         for j in range(len(nums)):
#             for i in range(len(nums)-1):
#                 if nums[i]>nums[i+1]:
#                     nums[i],nums[i+1]=nums[i+1],nums[i]
#         for j in range(1,len(nums)):
#                     if nums[j]!=nums[j-1]:
#                        print(nums[j-1])
#         print(nums[len(nums)-1])


