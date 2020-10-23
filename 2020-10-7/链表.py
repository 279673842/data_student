class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)
class link:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        cursor = self.head
        string = ""
        while cursor:
            string += "{}-->".format(cursor)
            cursor = cursor.next
        return string + "end"

    def get(self, index):
        cursor = self.head
        for i in range(1, index):
            cursor = cursor.next
        return cursor.next

    def insert(self, index, data):
        node = Node(data)
        if index < 0 or index > self.size:
            raise IndexError("超范围")
        elif self.size == 0:
            self.head = node
            self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = node

        elif index == self.size:
            self.tail.next = node
            self.tail = node
        else:
            prev = self.get(index-1)
            node.next = prev.next
            prev.next = node
        self.size += 1

    def remove(self, index: int):
        if __name__ == '__main__':
            if index < 0 or index >= self.size:
                raise IndexError("超范围")
            elif index == 0:
                cursor = self.head
                self.head = self.head.next
                remove = cursor
                cursor.next = None
            elif index == self.size - 1:
                cursor = self.get(index - 1)
                remove = cursor
                cursor.next = None
                self.tail = cursor
            else:
                cursor = self.get(index - 1)
                remove = cursor
                cursor.next = cursor.next.next
            self.size -= 1
            return remove

    def revers(self):
        if self.head:
            before = None
            start = self.head
            cursor = self.head
            while cursor:
                after = cursor.next
                cursor.next = before
                before = cursor
                cursor = after
            self.head = before
            self.tail = start

        else:
            return "空"







    def huan(self):
        self.tail.next=self.head.next
        cursor = self.head
        temp = self.head
        if cursor.next:
            while cursor:
                cursor = cursor.next
                temp = temp.next.next
                if temp is None or cursor is None:
                    return "不是环链表"
                elif cursor.next == temp.next.next:
                    return "是环链表"


li = link()
for i in range(5):
    li.insert(0, i)
print(li)
a = li.remove(0)
print(li)
print(a)
li.revers()
print(li)
# li.new_huan()
# print(li)
print(li.huan())
