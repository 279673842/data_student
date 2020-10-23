from typing import List
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "{}".format(self.val)
class Solution:
    def __init__(self):
        self.head = None

    def swapPairs(self, hea: Node) -> Node:
        self.head=hea
        if self.head == None or self.head.next==None:
            return self.head
        elif self.head.next.next==None:
            temp=self.head.next.next
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
    def __repr__(self):
        cursor = self.head
        string = ""
        while cursor:
            string += "{}-->".format(cursor)
            cursor = cursor.next
        return string + "end"



ll = Solution()
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    # node5 = Node(5)
    # node6 = Node(6)
    # node7 = Node(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next =None
    # node5.next = node6
    # node6.next = node7
    # node7.next = None
    # print(circle(node1))
    print(ll.swapPairs(node1))
    print(ll)

#
# ll = ListNode()
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n6 = ListNode(6)
# n7 = ListNode(7)
# n8 = ListNode(8)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n7
# n7.next = n8
# print(n1)