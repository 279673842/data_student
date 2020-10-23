# 27.移除值
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

from typing import  List
class delmn:
    def dels(self, nums:List, val):
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1

    # 快慢指针

# 283. 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。


class delmq:
    def dels(self, nums: List):
        fast=0
        slow=0
        while fast<len(nums):
            if nums[fast]==0:
                fast+=1
            else:
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
        for i in range(slow,len(nums)):
            nums[i]=0