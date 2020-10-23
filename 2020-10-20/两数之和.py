from typing import  List
def sumtwo2(nums:List,target):
    nums.sort()
    m=0
    n=len(nums)-1
    while m< n:
        if nums[m]+nums[n]==target:
            print(m,n)
        elif nums[m]+nums[n]>target:
            n-=1
        elif nums[m]+nums[n]<target:
            m+=1
def sumtwo2(nums:List,target):
    dic={}
    for i in range(len(nums)):
        if target-i in dic:
            return dic[target-i],i
        dic[nums[i]]=i

