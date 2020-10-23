# 209. 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
# 如果不存在符合条件的子数组，返回 0。
# 示例：
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        mins = len(nums)
        for j in range(len(nums) - 1):
            sums = 0
            count = 0
            for i in range(j, len(nums)):
                if sums <= s:
                    sums += nums[i]
                    count += 1
            if sums>=s:
                if count < mins:
                    mins = count
            else:
                if mins ==len(nums):
                    mins=0
        return mins

S = Solution()
# print(S.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(S.minSubArrayLen(100, []))
