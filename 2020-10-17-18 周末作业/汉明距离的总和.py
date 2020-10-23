# 477. 汉明距离总和
# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
# 计算一个数组中，任意两个数之间汉明距离的总和。
# 示例:
# 输入: 4, 14, 2
# 输出: 6
# 解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
# 所以答案为：HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
# 注意:数组中元素的范围为从 0到 10^9。数组的长度不超过 10^4。


from typing import List
def totalHammingDistance(nums:List):
    num = 0
    # for i in range(len(nums)-1):
    #     for j in range(i+1,len(nums)):
    #         m=nums[i]^nums[j]
    #         while m !=0:
    #             m=m&(m-1)
    #             num+=1
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            m = nums[i] ^ nums[j]
            num += str(bin(m)[2:]).count("1")

    return num



# 完整版
# def totalHammingDistance(self, nums):
#     return sum((b.count('0') * b.count('1')) for b in zip(*map('{:032b}'.format, nums)))

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        num=0
        for i in range(32):
            n=0
            for j in nums:
                n += (j >> i)&1
            num+=(len(nums)-n)*n
        return num

print(totalHammingDistance([4, 14, 2]))



# a=10101010
# # tem='%d' %a
# a=str(a)
# # print(tem,type(tem))
# # a.count()
# print(a,type(a))
# print(a.count("1"))
# print(bin(2^14)[2:])
