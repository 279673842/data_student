from typing import List


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)
# n=Node(1)
# print(n)


# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=None
#     def __repr__(self):
#         return "Node({})".format(self.data)


# class linklist():
#     def __init__(self):
#         self.head=None
#     def insert_head(self,data):
#         New_Node=Node(data)
#         if  self.head is not None:
#             New_Node.next=self.head
#         self.head=New_Node
#      def append(self,data):
#         if  self.head is None
#             self.insert_head(data)
#          else
#             temp=self.head
#             while temp.next is not  None:
#                 temp=temp.next
#             temp.next=Node(data)

# class linkedlist:
#     def __init__(self):
#         self.head = None
#
#     def insert_head(self, data):
#         new_node = Node(data)
#         if self.head is not None:
#             new_node.next = self.head
#         self.head = new_node
#
#     def append(self, data):
#         if self.head is None:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = Node(data)
#
#     def __repr__(self):
#         corsor = self.head
#         string = ""
#         while corsor:
#             string += "{}".format(corsor)
#             corsor = corsor.next
#         return string + "end"
#
#
# list = linkedlist()
# for i in range(10):
#     list.insert_head(i)
#
# print(list)


class linked:
    def __init__(self):
        self.head = None

    # 从头增加
    def insert_head(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node
    # 从尾增加

    def append(self, data):
        # new_node=Node(data)
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)

    def __repr__(self):
        corsor = self.head
        string = ""
        while corsor is not None:
            string += "{}".format(corsor)
            corsor = corsor.next
        return string + "end"
    # 按位置,插入单个数据

    def insert(self, i, data):
        corsor = self.head
        if corsor is None:
            self.insert_head(data)
        elif i == 1:
            self.insert_head(data)
        else:
            temp = self.head
            j = 1
            per = temp
            while j < i:
                per = temp
                temp = temp.next
                j += 1
            node = Node(data)
            per.next = node
            node.next = temp
# 插入列表

    def linklist(self, data: List):
        self.head = Node(data[0])
        temp = self.head
        for i in data[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next
    # def linklists(self,data:List):
    #     self.head=Node(data[0])
    #     temp=self.head
    #     for i in  data[1:]:
    #         node=Node(i)
    #         temp.next=node
    #         temp=temp.next
    # 删除头节点

    def dels(self):
        temp = self.head
        if temp:
            self.head = temp.next
            temp=None

    def delete_last(self):
        temp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
        else:
            return "空语句"

li = linked()
for i in range(5):
    li.insert_head(i)
    li.append(i)
print(li)
li.linklist(list(range(4)))
print(li)
li.dels()
print(li)
li.delete_last()
print(li)
li.insert(2,3)
print(li)
li.dels()
print(li)
