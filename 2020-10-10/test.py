from typing import List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f"{self.data}"
class solution:
    def __init__(self):
        self.head=None

    # 两两交换链表中的节点
    # def get_two(self,l1:Node,l2:Node):
    #     new=Node(0)
    #     prev=new
    #     while l1 and l2 :
    #         if l1.data>l2.data:
    #             prev.next=l2
    #             l2=l2.next
    #         else:
    #             prev.next=l1
    #             l1=l1.next
    #         prev=prev.next
    #     if l1 !=None:
    #         prev.next=l1
    #     else:
    #         prev.next=l2
    #     self.head=new.next
    #     return new.next

    def removes(self,nu:Node,vall):
        new=Node(0)
        new.next=nu
        head=new
        while new.next :
            if new.next.data==vall:
                new.next=new.next.next
            else:
                new=new.next
        return new.next



    def __repr__(self):
        cursor = self.head
        string = ""
        while cursor:
            string += "{}-->".format(cursor)
            cursor = cursor.next
        return string + "end"

ll = solution()
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next =None
    node5.next = node6
    node6.next = node7
    node7.next = None
    # print(circle(node1))
    print(ll.get_two(node1,node5))
    print(ll)
