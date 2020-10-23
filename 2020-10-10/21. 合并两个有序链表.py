# 21. 合并两个有序链表
# # 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# # 示例：
# #
# # 输入：1->2->4, 1->3->4
# # 输出：1->1->2->3->4->4
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def __repr__(self):
#         return "{}".format(self.val)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "Node({})".format(self.val)
class Solution:
    def __init__(self):
        self.head = None
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new=ListNode()
        prev=new
        while l1 and l2 :
            if l1.val<=l2.val:
                prev.next=l1
                l1=l1.next
            else:
                prev.next=l2
                l2=l2.next
            prev=prev.next
        if l1!=None:
            prev.next=l1
        else:
            prev.next=l2
        self.head=new.next
    def __repr__(self):
        cursor = self.head
        string = ""
        while cursor:
            string += "{}-->".format(cursor)
            cursor = cursor.next
        return string + "end"

ll = Solution()
if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next =None
    node5.next = node6
    node6.next = node7
    node7.next = None
    # print(circle(node1))
    print(ll.mergeTwoLists(node1,node5))
    print(ll)