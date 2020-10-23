# 方法1 二分查找法
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        longs = len(nums) - 1
        start = 0
        while start <= longs:
            curr = (start + longs) // 2
            if target > nums[curr]:
                start = curr + 1
            elif target < nums[curr]:
                longs = curr - 1
            elif target == nums[curr]:
                return curr
        return -1


# 方法2 递归二分查找
def search2(nums: List[int], target: int, start, end) -> int:

    if end > 0:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return search2(nums, target, start, mid - 1)
        else:
            return search2(nums, target, mid + 1, end)
    else:
        return -1
