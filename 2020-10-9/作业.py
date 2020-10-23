# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#     def __repr__(self):
#         return "Node({})".format(self.data)
# class link:
#     def __init__(self):
#         self.head=None
#         self.size=0
#
#     def remove(self,data):
#         node=Node(data)
#         if self.head:
#             curcor=self.head
#             for i in range(self.size):======没有
#                 if self.head==node:
#                     self.head.next=None
#                 elif curcor.next==node :
#                     curcor.next=curcor.next.next
#                 else:
#                     curcor=curcor.next
#
#         else:
#             raise IndexError("空")
#
#
# li=link()
# li.remove(1)
# print(li)


"""
Author:BAI先生
github:主页NONE
Create:2020/10/1011:08
"""

from typing import  List
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __repr__(self):
    #     return "{}".format(self.val)
class Solution:
    # def swapPairs(self, head: ListNode) -> ListNode:
    def __init__(self):
        self.head = None
    def swapPairs(self, hea: Node) -> Node:
        self.head=hea
        if self.head==None:
            return self.head
        elif self.head.next ==None:
             return self.head
        elif self.head.next.next==None:
            temp=self.head.next
            self.head.next=None
            temp.next=self.head
            self.head=temp
            return self.head
        else:
            temp=self.head.next
            n=self.head.next.next
            t=self.head.next
            p=self.head
            # n=t.next
            while  not(n == None or n.next == None) :#
                t.next=p
                t=n.next
                p.next=t
                p=n
                n=t.next
            t.next=p
            p.next=n
            self.head=temp
            return  self.head
li=Solution()

print(li.swapPairs([1,2,3,4]))
# lm=ListNode
# print(li.swapPairs([1,2,3,4]))


