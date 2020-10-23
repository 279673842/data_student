# from typing import List
#
#
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return "Node({})".format(self.data)
#
#
# class linkled:
#     # 设置一个头的属性
#     def __init__(self):
#         self.head = None
#     # 从头增加一个数
#
#     def insert_head(self, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             node.next = self.head
#     # 从尾增加一个数
#
#     def append(self, data):
#
#         if self.head is None:
#
#             self.insert_head(data)
#         else:
#             node = self.head
#             while node.next:
#                 node = node.next
#             node.next = Node(data)
#     # 对象数据显现
#
#     def __repr__(self):
#         corsor = self.head
#         string = ''
#         while corsor is not None:
#             string += "{}-->".format(corsor)
#             corsor = corsor.next
#         return string + "end"
#     # 按位置插入一个数据位置
#
#     def insert(self, i, data):
#         corsor = self.head
#         if corsor is None:
#             self.insert_head(data)
#         elif i == 1:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             j = 1
#             pre = temp
#             while j < i:
#                 pre = temp
#                 temp = temp.next
#                 j = j + 1
#             node = Node(data)
#             pre.next = node
#             node.next = temp
#
#     # 添加列表
#     def linklist(self, data: List):
#         self.head = Node(data[0])
#         temp = self.head
#         for i in data[1:]:
#             node = Node(i)
#             temp.next = node
#             temp = temp.next
#
#     # 删除第一个数据
#     def delm(self):
#         temp=self.head
#         if temp:
#             self.head=temp.next
# #
#     def del_last(self):
#         temp=self.head
#         if  self.head is not None:
#             if self.head.next is None:
#                 self.head = None
#             while temp.next.next:
#                 temp=temp.next
#             temp.next = None
#         else:
#             "空语句"
# li = linkled()
# li.insert_head(1)
# print(li)
# li.append(2)
# print(li)
# li.insert(2, 99)
# print(li)
# li.linklist([2,2,3,4,2,1,5,7])
# print(li)
# li.delm()
# print(li)
# li.del_last()
# print(li)


#
# from    typing import List
#
# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=None
#     def __repr__(self):
#         return "Node({})-->".format(self.data)
# class  link:
#     def __init__(self):
#         self.head=None
#     def __repr__(self):
#         corsor=self.head
#         string=""
#         while corsor is not None:
#             string+="{}".format(corsor)
#             corsor=corsor.next
#         return string+"end"
#     def insert_head(self,data):
#         corsor=Node(data)
#         if self.head is None:
#             self.head=corsor
#         else:
#             corsor.next=self.head
#         self.head=corsor
#     def append(self,data):
#
#         if self.head is None:
#             self.insert_head(data)
#
#         else:
#             corsor=self.head
#             while corsor.next:
#                 corsor=corsor.next
#             corsor.next=Node(data)
#
#     def insert(self,i,data):
#         # corsor=Node(data)
#         corsor=self.head
#         j=1
#         pre=corsor
#         while j<i:
#             pre = corsor
#             corsor=corsor.next
#             j+=1
#         node=Node(data)
#         pre.next=node
#         node.next=corsor
#     def link_list(self,data:List):
#         self.head=Node(data[0])
#         corsor=self.head
#         for i in data[1:]:
#             node=Node(i)
#             corsor.next=node
#             corsor=corsor.next
#
#     def dels(self):
#         corsor=self.head
#         if corsor:
#             self.head=corsor.next
#         corsor = None
#     def del_last(self):
#         corsor=self.head
#         while corsor.next.next:
#             corsor=corsor.next
#         corsor.next=None
#
#
# li=link()
# li.insert_head(1)
# print(li)
# li.insert_head(3)
# print(li)
# li.append(8)
# print(li)
# li.insert(2,5)
# print(li)
# li.link_list([1,2,4,71,2])
# print(li)
# li.dels()
# print(li)
# li.del_last()
# print(li)


from typing import  List
class Node:#建立节点类
    def __init__(self, data, next=None):#定义,接收data,和next默认None
        self.data = data
        self.next = None

    def __repr__(self):#定义repr
        return "Node({})-->".format(self.data)#返回打印


class link:#定义链表类
    def __init__(self):#定义
        self.head = None #属性 head的默认值为NOne

    def __repr__(self):
        corsor = self.head
        string = ""
        while corsor:
            string += "{}".format(corsor)
            corsor = corsor.next
        return string + "end"

    def insert_head(self, data):
        corsor = Node(data)
        if self.head:
            corsor.next = self.head
        self.head = corsor

    def append(self, data):
        corsor = self.head
        if corsor:
            while corsor.next:
                corsor = corsor.next
            corsor.next = Node(data)
        else:
            self.insert_head(data)

    def insert(self, i, data):
        corsor = self.head
        j = 1
        befor = corsor
        while j < i:
            befor = corsor
            corsor = corsor.next
            j+=1
        node = Node(data)
        befor.next = node
        node.next = corsor
    def linklist(self,data:List):
        self.head=Node(data[0])
        corsor=self.head
        for i in data[1:]:
            node=Node(i)
            corsor.next=node
            corsor=corsor.next

    def dels_head(self):
        corsor=self.head
        if corsor:
            self.head=corsor.next
            corsor.next=None
    def del_last(self):
        corsor=self.head
        while corsor.next.next:
            corsor=corsor.next
        corsor.next=None
    def linklis(self,data:List):
        self.head=Node(data[0])
        corsor=self.head
        for i in data[1:]:
            node=Node(i)
            corsor.next=node
            corsor=corsor.next
    def delss_head(self):
        corsor=self.head
        if corsor:
            self.head=corsor.next
            corsor.next=None
    def dels_last(self):
        corsor=self.head
        if corsor:
            if corsor.next is None:
                self.head = None
            else:
                while corsor.next.next:
                    corsor=corsor.next
                corsor.next=None
        else:
            "空"


    # def delm_last(self):
    #     corsor=self.head
    #     if corsor:
    #         if corsor.next:
    #             while corsor.next.next:
    #                 corsor=corsor.next
    #             corsor.next=None
    #         else:
    #             self.head=None
    #     else:
    #         return "空语句"


    def delm_last(self):
        corsor=self.head
        if corsor:
            if corsor.next:
                while  corsor.next.next:
                    corsor=corsor.next
                corsor.next=None
            else:
                self.head=None
        else:
            return "空语句"

    def revers(self):
        before=None#定义一个为空的指向
        cursor=self.head #链表的头赋予
        while cursor:#链表不空时循环
            after=cursor.next#
            cursor.next=before
            before=cursor
            cursor=after
        self.head=before

    def __getitem__(self,index):
        cursor=self.head
        if cursor is None:
            raise IndexError("链表为空")
        for _ in range(1,index):
            if cursor.next is None:
                raise IndexError("长度不足")
            else:
                cursor=cursor.next
        return cursor.next

    def get(self,index):
        return self.__getitem__(index)

    def __setitem__(self, index, value):
        cursor=self.head
        if cursor is None:
            raise IndexError("链表为空")
        for i in range(1,index):
            if cursor.next is None:
                raise IndexError("超范围")
            cursor=cursor.next
        cursor.data=value



li = link()
for i in range(4):
    li.insert_head(i)
print(li)
li.insert_head(1)
print(li)
li.append(22)
print(li)
li.insert(3, 208)
print(li)
li.linklist([1,2,4,5,71,2,5])
print(li)
li.dels_head()
print(li)
li.del_last()
print(li)
li.linklis([1,2,3,4,65,7,3,7])
print(li)
li.dels_head()
print(li)
li.dels_last()
print(li)
li.delm_last()
print(li)
li.revers()
print(li)
# li.__getitem__(2)
# print(li.__getitem__(2))
li.__setitem__(2,2)
print(li)

