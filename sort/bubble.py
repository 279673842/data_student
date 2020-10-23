from randomlist import randomlist
from typing import List
def bubble(nums:List):
    count = 0
    for i in range(len(nums) - 1):
        flag=True
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                flag=False
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                count += 1
                print("第%s轮排序结果" % (count), nums)
        if flag==True:
            return
    return nums

if __name__ == '__main__':
    mm=bubble(randomlist.randomlist(15))
    # mm=bubble([27, 43, 63, 71, 25, 62, 42, 73, 36, 32, 91, 95, 50, 46, 13])
    # print(mm)