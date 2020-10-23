from pprint import  pformat
class Node:
    def __init__(self,data,parent):
        self.data=data
        self.parent=parent
        self.right=None
        self.left=None
    def __repr__(self):
        if self.right is None and self.left is None :
            return f"{self.data}"
        return pformat({"%s" %(self.data):(self.left,self.right)},indent=1)# 缩进

class binarysearchtree:
    def __init__(self):
        self.root=None
    def __str__(self):
        return str(self.root)

    def insert(self,data):
        node=Node(data,None)
        if self.root is None:
            self.root=node
        else:
            temp=self.root
            while temp:
                if data>temp.data:
                    if temp.right is None:
                        temp.right=node
                        break
                    else:
                        temp=temp.right
                elif data <temp.data:
                    if temp.left is None:
                        temp.left=node
                        break
                    else:
                        temp=temp.left
                node.parent=temp
    def insers(self,*values):
        for value in values:
            self.insert(value)
        return self
    def search(self,data):
        if self.root is None:
            raise IndexError ("EMPTY")
        else:
            temp=self.root
            while temp and temp.data != data:
                if data >temp.data:
                    temp=temp.right
                elif data < temp.data:
                    temp=temp.left
            return temp

    def remove(self,data):
        node=self.search(data)
        if node.right is None and node.left is None:
            self._reassign(node,None)
        elif node.right is None:
            self._reassign(node,node.left)
        elif node.left is None:
            self._reassign(node,node.right)
        else:
            node_pop=self.get_max(node.left)
            self.remove(node_pop.data)
            node.data=node_pop.data

    def _reassign(self, node, childern):
        if childern is not None:
            childern.parent=node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right=childern
            else:
                node.parent.left=childern
        else:
            self.root=childern

    def get_max(self, node):
        if node is  None:
            node=self.root
        while node.right:
            node=node.right

    def is_right(self,node):
        return  node==node.parent.right


    # 递归前序,中序
    def deeppreorder(self,node):
        if node is None:
            return None
        print(node)
        self.deeppreorder(node.right)
        self.deeppreorder(node.left)

    def deepinorder(self,node):
        if node is None:
            return None
        self.deepinorder(node.right)
        print(node)
        self.deepinorder(node.left)
    #前序方法1
    def preorder(self,node):
        stack=[]
        while node and len(stack)>0:
            while node :
                print(node)
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                node=node.right
     # 前序方法2
    def preorder2(self,node):
        stack=[node]
        while len(stack):

            print(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()
    #中序
    def inorder(self,node):
        stack = []
        while node and len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node)
                node = node.right
    # 后序
    def postorder(self,node):
        stack1=[]
        stack2=[]
        stack1.append(node)
        while len(stack1)>0:
            temp=stack1.pop()
            if temp.right:
                stack1.append(temp.right)
            if temp.left:
                stack1.append(temp.left)

            stack2.append(temp)
        while stack2:
            print(stack2.pop())
    # 层序输出 (数组方法)
    def cengxu(self,node):
        if node is None:
            raise  IndexError("empty")
        else:
            stack=[node]
            while len(stack)>0:
                node=stack.pop(0)
                print(node)
                if node.left:
                    stack.append(node.left)
                if node.left:
                    stack.append(node.right)


    # def cengxu2(self,node):
    #     from queue import Queue
    #     if node is None:
    #         raise IndexError("empty")
    #     else:
    #         q=Queue


if __name__ == '__main__':
    t = binarysearchtree()
    t.insers(6,1,3,2,5,4,8)
    # t.insert(4)
    print(t)
    # t.insert(4)
    # t.insert(2)
    # t.insert(1)
    # t.insert(3)
    # t.insert(15)
    # t.insert(14)
    # t.insert(16)
    # t.insert(4)
    # t.search(4)
    # print(t.search(14))
    print(t)
    # t.remove(14)
    # print(t)
    # t.remove(16)
    # print(t)
    # t.remove(4)
    # t.deeppreonder(t.root)
    # print(t)
    # t.indeeppreonder(t.root)
