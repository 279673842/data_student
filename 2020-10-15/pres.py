from pprint import  pformat
class Node:
    def __init__(self,data,parent):
        self.data=data
        self.parent=parent
        self.right=None
        self.left=None
    def __repr__(self):
        if self.left is None and self.right is None :
            return f"{self.data}"
        return pformat({"%s" %(self.data):(self.right,self.left)},indent=1)
class binarysearchtree:
    def __init__(self):
        self.root=None
    def __str__(self):
        return str(self.root)

    def deeppreorder(self,node):
        if not node:
            return None
        self.deeppreorder(node.right)
        print(node.data)
        self.deeppreorder(node.left)
    def preorder(self,node):
        stack=[node]
        while len(stack)>0:
            print(node.data)
            if node.left:
                stack.append( node.left)
            if node.right:
                stack.append(node.right)
            node = stack.pop()
    def deepinorder(self,node):
        if not node :
            return None
        self.deepinorder(node.left)
        print(node.data)
        self.deepinorder(node.right)

    def inorder(self,node):
        stack=[]
        while node and len(stack)>0:
            while node.left:
                stack.append(node.left)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                print(node.data)
                node=node.right

