# 611. 有效三角形的个数
# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
# 示例 1:
# 输入: [2,2,3,4]
# 输出: 3
# 解释:有效的组合是: 2,3,4 (使用第一个 2)  2,3,4 (使用第二个 2) 2,2,3
# 注意:数组长度不超过1000。数组里整数的范围为 [0, 1000]。
from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for right in range(2,len(nums)):
            left=0
            curr=right-1
            while left < right:
                if nums[left]+nums[curr]>nums[right]:
                    count+=right-left
                    right-=1
                else:
                    left+=1
        return count









# from typing import List
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         mm=[]
        # for i in range(len(nums)):
        #     left=i+1
        #     right=len(nums)-1
        #     while left<right:
        #         if nums[i]+nums[left]>nums[right] and 2*(nums[i]+nums[left])>nums[right]:
        #             mm.append([nums[i],nums[left],nums[right]])
        #             if nums[left]==nums[left+1]:
        #                 left+=1
        #             elif nums[right]==nums[right-1]:
        #                 right-=1
        #             else:
        #                 left+=1
        #                 right-=1
        #         elif nums[i]+nums[left]<nums[right] and 2*(nums[i]+nums[left])>nums[right]:
        #             left+=1
        #         elif nums[i]+nums[left]<nums[right] and 2*(nums[i]+nums[left])<nums[right]:
        #             right-=1
        #         else:
        #             right-=1
        # return mm
#
# s=Solution()
# print(s.triangleNumber([2, 2, 3, 4]))