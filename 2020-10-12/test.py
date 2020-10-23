class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class concat:
    def hebing(self, l1: Node, l2: Node):
        new = Node(0)
        start = new
        while l1 and l2:
            if l1.data < l2.data:
                new.next = Node(l1)
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
        if l1 is None:
            new.next = l2
        else:
            new.next = l1
        return start.next


class concat2:
    def hebing(self, l1: Node, l2: Node):
        new = Node(0)
        start = new
        while l1 or l2:
            if l1 is None:
                new.next = l2
                break
            elif l2 is None:
                new.next = l1
                break
            elif l1.data < l2.data:
                new.next = Node(l1.data)
                l1 = l1.next
            else:
                new.next = l1
                new.next = Node(l2.data)
                l2 = l2.next
            new = new.next
            return start.next


class Stack:
    def __init__(self):
        self.top = []
        self.size = 0
    def __repr__(self):
        return self.top
    def push(self, data):
        self.top.append(data)
        self.size -= 1
    def pop(self):
        if self.top:
            temp=self.top.pop()
        else:
            raise IndexError("stack is emtpy")
        return  temp


class Stack2:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self,data):
        node=Node(data)
        if self.top:
            node.next=self.top
            self.top=node
        else:
            self.top=data
        self.size+=1
    def pop(self):
        if self.top:
            temp=self.top
            self.top = self.top.next
            self.top.next=None
        else:
            raise IndexError("pop from an emtpy stack")
        self.size -= 1
        return temp
        