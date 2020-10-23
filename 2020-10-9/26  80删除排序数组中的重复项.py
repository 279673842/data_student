# 26.   快慢指针
# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

from typing import List


class delmm:
    def dels(self, nums: List):
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1
# 80. 删除排序数组中的重复项 II
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。


class del_two:
    def dels(self, nums):
        fast = 1
        slow = 0
        count = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                count += 1
                fast += 1
                if count == 2:
                    slow += 1
                    nums[slow] = nums[fast]
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
                count=1
