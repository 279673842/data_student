

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)


class link:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def circle(head: Node):
    fast = head
    slower = head
    while fast and fast.next:
        fast = fast.next.next
        slower = slower.next
        if fast == slower:
            break
    while slower != fast:
        slower = slower.next
        fast = fast.next
    return slower


def circle2(head: Node):
    fast = head
    slower = head
    while fast and fast.next:
        fast = fast.next.next
        slower = slower.next
        if fast == slower:
            while slower != fast:
                slower = slower.next
                fast = fast.next
            return slower

    # slower=head
    # while slower:
    #     slower=slower.next
    #     fast=fast.next
    #     if slower==fast:
    #         return slower


# 数组
class Aeeay:
    def __init__(self, sapacity):
        self.array = [None] * sapacity
        self.size = 0
    def addsapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        return new_array
    def insert(self, index, element):
        if index < 0:  # or index>self.size:
            raise IndexError("超限")
        if index >= len(self.array) or self.size == len(self.array):
            self.addsapacity()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1
    def remove(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("超限")
        if self.size == len(self.array):
            self.addsapacity()
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1
