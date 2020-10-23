from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data=data
        self.parent=parent
        self.right=None
        self.left=None
    def __repr__(self):
        return pformat({"%s" %(self.data):(self.right,self.left)})

class Binarytree:
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
                if data >=temp.data:
                    if temp.right:
                        temp=temp.right
                    else:
                        temp.right=node
                        break
                elif data <temp.data:
                    if temp.left:
                        temp=temp.left
                    else:
                        temp.left=node
                        break
                node.parent=temp
    def search(self,data):
        if self.root is None:
            raise IndexError("EMPTY")
        else:
            temp=self.root
            while temp and temp.data !=data:
                if data >temp.data:
                    temp=temp.right
                elif data < temp.data:
                    temp =temp.left
            return temp

    # 前序递归遍历
    def deeppreonder(self, node):
        if not node:
            return None
        print(node.data)
        self.deeppreonder(node.left)
        self.deeppreonder(node.right)

    # 前序遍历
    def preonder(self,node):
        stack=[node]
        while len(stack) >0:
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node=stack.pop()
    # 中序递归
    def indeeppreonder(self, node):
        if not node:
            return None

        self.deeppreonder(node.left)
        print(node.data)
        self.deeppreonder(node.right)
    # 中序遍历
    def onder(self,node):
        stack = []
        while node or len(stack) >0:
            while node:
                stack.append(node)
                node=node.left
            if len(stack) >0:
                node =stack.pop()
                print(node.data)
                node =node.right

# if __name__ == '__main__':
#     t = Binarytree()
#     t.insert(4)
#     t.insert(2)
#     t.insert(1)
#     t.insert(3)
#     t.insert(15)
#     t.insert(14)
#     t.insert(16)
#     t.insert(4)
#     t.search(4)
#     print(t.search(14))
#     print(t)
#     # t.remove(14)
#     # print(t)
#     # t.remove(16)
#     # print(t)
#     # t.remove(4)
#     t.deeppreonder(t.root)
#     print(t)
#     t.indeeppreonder(t.root)

