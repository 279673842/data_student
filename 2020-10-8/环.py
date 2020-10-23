class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "Node({})".format(self.data)
#
def circle(head: Node):
    fast = head
    slower = head
    while fast and fast.next:
        fast = fast.next.next
        slower = slower.next
        if fast == slower:
            return True
    return False
# def circle(head:Node):
#     fast = head
#     slower = head
#     while fast and fast.next:
#         fast = fast.next.next
#         slower = slower.next
#         if fast == slower:
#             break
#     slower = head
#     while slower != fast:
#         slower = slower.next
#         fast = fast.next
#     return slower
#
#
def circle_dian(head: Node):
    fast = head
    slower = head
    while fast and fast.next:
        fast = fast.next.next
        slower = slower.next
        if fast == slower:
            break
    slower = head
    while slower != fast:
        slower = slower.next
        fast = fast.next
    return slower
#
#
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node2
    print(circle(node1))
    print(circle_dian(node1))

#
#
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#     def __repr__(self):
#         return "Node({})",format(self.data)
#
#
# # def circle(head:Node):
#
#
#
#
# #
# from typing import List
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#
#         for j in nums:
#             if j==val:
#                 nums.remove(j)
#         for j in range(len(nums)-1):
#             if nums[j]==val:
#                 nums.pop(j)
#                 len(nums) -1
#         if val in nums:
#             # for j in range(len(nums) - 1):
#             #     if nums[j] == val:
#             #         nums.remove(nums[j])
#             #         len(nums) - 1
#             for j in nums:
#                 if j == val:
#                     nums.remove(j)
#
#
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        for j in range(len(nums)-1):
            for i in range(j+1,len(nums)):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
               print(nums[i-1])

lis=Solution()
print(lis.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))