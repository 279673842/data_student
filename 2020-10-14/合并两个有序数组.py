# 合并两个有序数组
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int,
              nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        s = m + n - 1
        while i > 0 and j > 0 and s > 0:
            if nums1[i] < nums2[j]:
                nums1[s] = nums2[j]
                j -= 1
            elif nums1[i] > nums2[j]:
                nums1[s] = nums1[i]
                i-=1
            elif nums1[i] == nums2[j]:
                nums1[s] = nums2[j]
                j += 1
            s -= 1
            while n - 1 - j >= 0:
                nums1[s] = nums2[j]
                j -= 1
        return nums1
        # j=0
        # for i in nums2:
        #     nums1[m+j]=i
        #     j+=1
        # nums1.sort()