# class Node:
#     def __init__(self, data,next = None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return "Node({})".format(self.data)
#
#
# class link:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def __repr__(self):
#         cursor = self.head
#         string = ""
#         while cursor:
#             string += "{}-->".format(cursor)
#             cursor = cursor.next
#         return string + "end"
#
#     def get(self, index):
#         cursor = self.head
#         for i in range(1, index):
#             cursor = cursor.next
#         return cursor
#
#     # def set(self, index, data):
#     #     cursor = self.head
#     #     for i in range(1, index):
#     #         if cursor.next:
#     #             cursor = cursor.next.next
#     #         self.data = data
#
#     def insert(self, index, data):
#         node = Node(data)
#         if index < 0 or index > self.size:
#             raise IndexError("超出范围")
#         elif self.head is None:
#             self.head = node
#             self.tail = node
#         elif index == 0:
#             node.next = self.head
#             self.head = node
#         elif index == self.size:
#             self.tail.next = node
#             self.tail = node
#
#         else:
#             cursor = self.get(index - 1)
#             temp = cursor.next
#             cursor.next = node
#             node.next = temp
#         self.size += 1
#
#     def remove(self, index: int):
#         if index < 0 or index > self.size:
#             raise IndexError("超出范围")
#         elif self.head is None:
#             raise IndexError("链表为空")
#         elif index == 0:
#             rmove = self.head
#             cursor = self.head.next
#             self.head = cursor
#         elif index == self.size:
#             cursor = self.get(index - 1)
#             cursor.next = None
#             rmove = self.tail
#             self.tail = cursor
#         else:
#             cursor = self.get(index - 1)
#             rmove = cursor.next
#             cursor.next = cursor.next.next
#         self.size -= 1
#         return rmove
#
#     def revers(self):
#         if self.head:
#             befor = None
#             cursor = self.head
#             taile = self.tail
#             while cursor:
#                 after = cursor.next
#                 cursor.next = befor
#                 befor = cursor
#                 cursor = after
#             self.head = befor
#             self.tail = taile
#         else:
#             return "空链表"
#
#     def revers_del(self, num):
#         self.revers()
#         self.remove(num)
#         self.revers()
#     def ifhuan(self):
#         self.tail.next=self.head.next
#         cursor = self.head
#         temp = self.head
#         if cursor.next:
#             while cursor:
#                 cursor = cursor.next
#                 temp = temp.next.next
#                 if temp is None or cursor is None:
#                     return "不是环链表"
#                 elif cursor.next == temp.next.next:
#                     return ["是环链表",temp.next.next]
#
#     def dian1(self):
#         self.tail.next=self.head.next
#         cursor = self.head
#         temp = self.head
#         if cursor.next:
#             while cursor:
#                 cursor = cursor.next
#                 temp = temp.next.next
#                 if temp is None or cursor is None:
#                     return False
#                 elif cursor.next == temp.next.next:
#                     return temp.next.next
#     def dian2(self):
#         self.tail.next = self.head.next
#         cursor = self.head
#         temp = self.dian1()
#         while cursor:
#             if cursor == temp:
#                 return cursor
#             cursor = cursor.next
#             temp = temp.next
#
# #
# li=link()
# for i in range(5):
#     li.insert(0, i)
# print(li)
# li.insert(5, 9)
# print(li)
# li.insert(3, 8)
# print(li)
# print(li.remove(3))
# print(li)
# # li.revers()
# # print(li)
# # li.revers_del(2)
# # print(li)
#
# print(li.ifhuan())
# print(li.dian2())


class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)
class link:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def __repr__(self):
        cursor=self.head
        string=""
        while cursor:
            string+=f"{cursor}"
            cursor=cursor.next
        return  string+"end"
    def get(self,index):
        cursor=self.head
        for i in range(1,index):
            cursor=cursor.next
        return cursor.next
    def insert(self,index,data):
        node=Node(data)
        if index<0 or index >self.size:
            raise  IndexError("长度超限")
        elif self.size ==0:
            self.head=node
            self.tail=node
        elif index==0:
            node.next=self.head
            self.head=node
        elif index==self.size:
            self.tail.next=node
            self.tail=node
        else:
            cursor=self.get(index-1)
            node.next=cursor.next
            cursor.next=node
        self.size+=1

    def remove(self,index):
        if index<0 or index >=self.size:
            raise  IndexError("长度超限")
        elif self.size ==0:
            raise IndexError("空链表")
        elif index==0:
            cursor=self.head.next
            self.head.next=None
            remove_node=self.head
            self.head=cursor
        elif index==self.size:
            cursor=self.get(index-1)
            remove_node = self.tail
            cursor.next=None
        else:
            cursor=self.get(index-1)
            remove_node =cursor.next
            cursor.next=cursor.next.next
        self.size-=1
        return remove_node
    def set(self,index,data):
        cursor=self.head
        for i in range(index):
            cursor=cursor.next
        self.data=data

    def revers(self):
        cursor=self.head
        temp = self.head
        berfore=None
        while cursor:
            after=cursor.next
            cursor.next=berfore
            berfore=cursor
            cursor=after
        self.head=berfore
        self.tail=temp

    def get(self, index):
        cursor = self.head
        for i in range(1, index):
            cursor = cursor.next
        return cursor.next
    def set(self, index, data):
        cursor = self.head
        for i in range(index):
            cursor = cursor.next
        self.data = data