# p=str([1,2,3])[1:-1]
# print(p)
# print(str([1,2,3])[1:1])

# class queue:
#     def __init__(self):
#         self.entries = [1, 2, 3, 4, 5, 6]
#         self.size = 6
#
#
#     def enqueue(self,data):
#         self.entries.append(data)
#     def dequeue(self):
#         self.entries=self.entries[1:]
#         return self.entries
#     def get(self, index):
# #         if self.entries:
# #             if self.size > index and index > 0:
# #                 temp = self.entries[index]
#             else:
#                 raise IndexError("11")
#         else:
#             raise IndexError("empty")
#         return temp
#
#     def set(self, index, data):
#         if self.entries:
#             if self.size > index and index >=0:
#                 self.entries[index] = data
#             else:
#                 raise IndexError(" ")
#         else:
#             raise IndexError(" empty ")
#         return data
#
#     def revers(self):
#         if self.entries is not None:
#             # for i in range(self.size-1,-1,1):
#             # self.entries = self.entries[-1:-1, -1]
#             self.entries.reverse()
#         else:
#             raise IndexError(" empty ")
#
#     def __repr__(self):
#         printb = "<" + str(self.entries)[1:-1] + ">"
#         return printb
#
#
# q = queue()
# q.revers()
# print(q)
# print(q.get(1))
# print(q.set(0,2))
# print(q)
# print(q.revers())
# q.set(0,2)
# q.printa()
# print(q)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class Linkqueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        curr = self.head
        str_q = ''
        while curr:
            str_q += f"{curr}-->"
            curr = curr.next
        return str_q + "end"

    def isempty(self):
        return self.head is None

    def enqueue(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("empty dequeue")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None


if __name__ == '__main__':
    q = Linkqueue()
    print(q.isempty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
