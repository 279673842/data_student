# 16. #最接近的三数之和
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
# 返回这三个数的和。假定每组输入只存在唯一答案。
# 示例：
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        num=abs(nums[0]+nums[1]+nums[-1]-target)
        he=nums[0]+nums[1]+nums[-1]
        for i in range(len(nums)-2):
            if i >0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j< k:
                result=nums[i]+nums[j]+nums[k]
                if result==target:
                    return result
                else:
                    res=abs(result-target)
                    if res<num:
                        num=res
                        he=result
                    if result<target:
                        j+=1
                    if result>target:
                        k-=1
        return he