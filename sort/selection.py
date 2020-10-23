from randomlist import randomlist
from typing import List
def selection(nums:List):
    count=0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
                count += 1
                print("第%s轮排序结果" % (count), nums)


if __name__ == '__main__':
    mm=selection(randomlist.randomlist(10))
    # print(mm)

def selection(nums:List):
    count=0
    for i in range(len(nums)-1):
        min_index=i
        for j in range(i+1,len(nums)):
            if nums[min_index]>nums[j]:
                min_index=j
                count += 1
                print("第%s轮排序结果" % (count), nums)
        nums[i],nums[min_index]=nums[min_index],nums[i]

if __name__ == '__main__':
    mm=selection(randomlist.randomlist(10))