# from typing import  List
# def insertsort(nums:List):
#     if len(nums)<2:
#         return nums
#     for right in range(1,len(nums)):
#         target=nums[right]
#         for i in range(0,right):
#             if target<nums[i]:
#                 nums[i+1:right+1]=nums[i:right]
#                 nums[i]=target
#                 break
#     return nums
# print(insertsort([9, 2, 5, 3, 7, 8, 1, 4]))

# class ListNode:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#     def __repr__(self):
#         return f"{self.data}"
# class Solution:
#     def __init__(self):
#         self.head=None
#
#
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         dummy=ListNode(0)
#         pre=dummy
#         cur=head
#         while cur:
#             temp=cur.next
#             while pre.next and pre.next.data<cur.data:
#                 pre=pre.next
#             cur.next=pre.next
#             pre.next=cur
#             cur=temp
#             pre=dummy
#         self.head=dummy.next
#         return self.head
#     def __repr__(self):
#         cursor = self.head
#         string = ""
#         while cursor:
#             string += "{}-->".format(cursor)
#             cursor = cursor.next
#         return string + "end"
def output(node):
    cursor = node
    string = ""
    while cursor:
        string += "{}-->".format(cursor)
        cursor = cursor.next
    return string + "end"
from typing import  List
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"{self.data}"


def insertsort(nums: List):
    if len(nums)<2:
        return nums
    for right in range(1,len(nums)):
        terget=nums[right]
        for i in range(0,right):
            if terget<nums[i]:
                nums[i+1:right+1]=nums[i:right]
                nums[i]=terget
                break
        return nums

def insertsort2(head:ListNode):
    dummy=ListNode(0)
    pre=dummy
    cur=head
    while cur:
        temp=cur.next
        while pre.next and pre.next.data>cur.data:
            pre=pre.next
        cur.next=pre.next
        pre.next=cur
        cur=temp
        pre=dummy
    return dummy.next














# def insertsort(nums:List):
#     if len(nums)<2:
#         return nums
#     for right in range(1,len(nums)):
#         target=nums[right]
#         for i in range(0,right):
#             if target<nums[i]:
#                 nums[i+1:right+1]=nums[i:right]
#                 nums[i]=target
#                 break
#     return nums
# def insertsortlist(head):
#     dummy=ListNode(0)
#     pre=dummy
#     cur=head
#     while cur:
#         temp=cur.next
#         while pre.next and pre.next.data<cur.data:
#             pre=pre.next
#         cur.next=pre.next
#         pre.next=cur
#         cur=temp
#         pre=dummy
#     return dummy.next


if __name__ == '__main__':
    l1 = ListNode(3)
    l2 = ListNode(3)
    l3 = ListNode(2)
    l4 = ListNode(1)
    l5 = ListNode(9)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = None

    # S = Solution()
    # print(S.insertionSortList(l1))
    # print(output(S.insertionSortList(l1)))
    # print(S.head)
