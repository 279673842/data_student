# 75. 颜色分类
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
# 示例:
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
from typing import  List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a=c=0
        b=len(nums)-1
        while c<=b:
            if nums[c]==0:
                nums[a],nums[c]=nums[c],nums[a]
                a+=1
                c+=1
            elif nums[c]==2:
                nums[b], nums[c] = nums[c], nums[b]
                b-=1
            else:
                c+=1
        print(nums)

l=Solution()
l.sortColors([2,0,2,1,1,0])