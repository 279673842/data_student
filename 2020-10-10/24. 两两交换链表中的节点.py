# 24. 两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def swapPairs(self, head: ListNode) -> ListNode:
    def swapPairs(self, head: Node) -> Node:
        dummp=Node(0)
        dummp.next=head
        pre=dummp
        while pre.next.next and pre.next:
            fast=pre.next.next
            slow=pre.next
            pre.next=fast
            slow.next=fast.next
            fast.next=slow
            pre=slow
        return dummp























# 自己做的
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     # def __repr__(self):
#     #     return "{}".format(self.val)
# class Solution:
#     # def swapPairs(self, head: ListNode) -> ListNode:
#     def __init__(self):
#         self.head = None
#     def swapPairs(self, hea: Node) -> Node:
#         self.head=hea
#         if self.head==None:
#             return self.head
#         elif self.head.next ==None:
#              return self.head
#         elif self.head.next.next==None:
#             temp=self.head.next
#             self.head.next=None
#             temp.next=self.head
#             self.head=temp
#             return self.head
#         else:
#             temp=self.head.next
#             n=self.head.next.next
#             t=self.head.next
#             p=self.head
#             # n=t.next
#             while  not(n == None or n.next == None) :#
#                 t.next=p
#                 t=n.next
#                 p.next=t
#                 p=n
#                 n=t.next
#             t.next=p
#             p.next=n
#             self.head=temp
#             return  self.head