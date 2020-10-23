class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)


class Link:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        cursor = self.head
        string = ""
        while cursor:
            string += f"{cursor}"
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
            raise IndexError("超出范围")
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
            prev = self.get(index - 1)
            node.next = prev.next
            prev.next = node
        self.size += 1

    def remove(self, index):

        if index < 0 or index >= self.size:
            raise IndexError("超出范围")
        elif self.size == 0:
            raise IndexError("空链表")
        elif index == 0:
            cursor = self.head.next
            removes = self.head
            self.head = cursor
        elif index == self.size - 1:
            temp = self.get(index - 1)
            removes = self.tail
            temp.next = None
            self.tail = temp
        else:
            temp = self.get(index - 1)
            remove = temp.next
            temp.next = temp.next.next
        self.size -= 1

    def reverse(self):
        berfore = None
        temp = self.head
        cursor = self.head
        while cursor:
            after = cursor.next
            cursor.next = berfore
            befroe = cursor
            cursor = after
        self.head = berfore
        self.tail = temp
li=Node()
print(Node([1,2,3,4]))