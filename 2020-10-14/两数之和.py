# class Node:
# #     def __init__(self,data):
# #         self.data=data
# #         self.next=None



# 方法1:暴力解法
def sumtwo(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                print(i,j)
# 方法2:对撞指针
def sumtwo2(nums,target):
    nums.sort()
    i=0
    j=len(nums)-1
    # for i in range(len(nums)):
    while i<j:
        if nums[i]+nums[j]==target:
            i+=1
            j-=1
            print(i,j)
        elif nums[i]+nums[j]>target:
            j-=1
        elif nums[i]+nums[j]<target:
            i+=1
# 方法3:哈希表法
def suntwo3(nums,target):
    dic={}
    for i in range(len(nums)):
        if target-nums[i] in dic:
            return dic[target-nums[i]],i
        dic[nums[i]]=i




# 三数之和:for 循环每次循环时,执行对撞指针.
from typing import  List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            while i>0 and nums[i]==nums[i-1]:
                continue
            while nums[i]>0:
                break
            j=i+1
            k=len(nums)-1
            while j< k:
                result=nums[i]+nums[j]+nums[k]
                if result >0:
                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                elif result<0:
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                elif result == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        continue
                    while j<k and nums[k] == nums[k+1]:
                        continue
# 三数之和:for 循环每次循环时,执行对撞指针.
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):

            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            j=i+1
            k=len(nums)-1
            while j< k:
                result=nums[i]+nums[j]+nums[k]
                if result >0:
                    k-=1
                    # while j<k and nums[k] == nums[k+1]:
                    #     k-=1
                elif result<0:
                    j+=1
                    # while j<k and nums[j] == nums[j-1]:
                    #     j+=1
                elif result == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return res