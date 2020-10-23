# 147. 对链表进行插入排序
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

# from typing import  List
# # 数组
# def insertsort(nums:List):
#     if len(nums)<2:
#         return nums
#     for right in range(1,len(nums)):
#         target=nums[right]
#         for i in range(0,right):
#             if target< nums[i]:
#                 nums[i+1:right+1]=nums[i:right]
#                 nums[i]=target
#                 break
#     return nums
# print(insertsort([9, 2, 5, 3, 7, 8, 1, 4]))
# 链表
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"

class Solution:
    def __init__(self):
        self.root=None
    def __repr__(self):
        return f"{self.root}"
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        pre = dummy
        cur = head
        while cur:
            temp = cur.next
            while pre.next and pre.next.data < cur.data:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            cur = temp
            pre = dummy
            self.root = dummy.next
        return self.root


if __name__ == '__main__':
    l1 = ListNode(0)
    l2 = ListNode(3)
    l3 = ListNode(2)
    l4 = ListNode(1)
    l5 = ListNode(9)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = None

    S = Solution()
    print(S.insertionSortList(l1))
