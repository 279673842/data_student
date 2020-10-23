

# =============================列表[]做栈==============


from typing import  List
class stack:
    def __init__(self):
        self.stack=[]
        self.size=0
    def push(self,data):
        self.stack.append(data)
        self.size+=1
    def pushs(self,data:List):
        self.stack.extend(data)
        self.size+=len(data)
    def pop(self):
        if self.stack:
            temp=self.stack.pop()
            self.size -= 1
            return temp
        else:
            raise IndexError("pop from an empty stack")
    def peek(self):
        if self.stack:
            return self.stack[-1]
    def sizeof(self):
        return self.size
    def output(self):
        for i in range(self.size-1,-1,-1):
            # a=self.stack
            # print(a.pop())
            print(self.stack[i])
    # def __repr__(self):
    #     return self.stack
#
#
# # an =[1,2,3,4,5,6,7]
# # print(an.pop())
# mm=stack()
# # mm.pushs([1,2,3,4,5,6,7])
# # print(mm)
# mm.push(1)
# mm.push(2)
# mm.push(3)
# mm.push(4)
# # mm.output()
# # mm.pushs([1,2,3,4,5,6,7])
# # mm.output()
# mm.pop()
# print(mm.peek())
# print(mm.sizeof())
#
# mm.output()




#=============================链表做栈=================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "Node({})".format(self.data)
class stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, data):
        node=Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1
    def pop(self):
        if self.top is None:
            raise  IndexError("栈为空")
        else:
            node=self.top
            self.top=self.top.next
            node.next=None
            return node



list = stack()
