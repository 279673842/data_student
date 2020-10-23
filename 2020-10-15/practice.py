from pprint import  pformat
class Node:
    def __init__(self,data,parent):
        self.data=data
        self.parent=parent
        self.right=None
        self.left=None
    def __repr__(self):
        if self.right is None and self.left is None:
            return f"{self.data}"
        return pformat({"%s"%(self.data):(self.left,self.right)},indent=1)

class binarytree:
    def __init__(self):
        self.root=None
    def __str__(self):
        return str(self.root)
    def deeppreorder(self,node):
        if not node:
            return None
        print(node)
        self.deeppreorder(node.right)
        self.deeppreorder(node.left)
    def preorder(self,node):
        stack=[node]
        while len(stack)>0:
            print(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node=stack.pop()
    def preorder2(self,node):
        stack=[]
        while node or len(stack)>0:
            while node:
                print(node)
                stack.append(node)
                node=node.left

            if len(stack):
                node=stack.pop()
                node=node.right

    def inorder(self, node):
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack):
                node = stack.pop()
                print(node)
                node = node.right
    def deepinorder(self,node):
        if not node:
            return None
        self.deepinorder(node.right)
        print(node)
        self.deepinorder(node.left)


    def innorder(self,node):
        stack=[]
        while node or len(stack)>0:
            while node:
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                print(node)
                node=node.right
    def preeorder(self,node):
        stack=[]
        while node or len(stack)>0:
            while node:
                print(node)
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                node=node.right
    def insert(self,data):
        node=Node(data,None)
        if self.root is None:
            self.root=node
        else:
            temp=self.root
            while node:
                if data >=temp.data:
                    if temp.right:
                        temp=temp.right
                    else:
                        temp.right=node
                elif data < temp.data:
                    if temp.left :
                        temp=temp.left
                    else:
                        temp.left=node
            node.parent=temp
    def search(self,data):
        if self.root is None:
            raise  IndexError("empy")
        else:
            temp=self.root
            while temp and temp.data !=data:
                if data>temp.data:
                    temp=temp.right
                elif data <temp.data:
                    temp=temp.left
    def remove(self,data):
        node=self.search(data)
        if node.right is None and node.left is None:
            self._reassign(node,None)
        elif node.right is None:
            self._reassign(node, node.right)
        elif node.left is None:
            self._reassign(node.node.right)
        else:
            temp=self.get_max(node.left)
            self.remove(temp.data)
            node.data=temp.data



    def _reassign(self, node, childern):
        if childern is not None:
            childern.parent=node.parent
        if node.parent is not  None:
            if self.is_right(node):
                node.parent.right=childern
            else:
                node.parent.left = childern
        else:
            self.root=childern

    def get_max(self, node):
        if node is None :
            node=self.root
        if self.root :
            while node.right:
                node=node.right
        return  node


    def is_right(self,node):
        return node==node.parent.right

    def deepspreorder(self,node):
        if node is None:
            return None
        print(node)
        self.deepspreorder(node.right)
        self.deepspreorder(node.left)
    def deepsinorder(self,node):
        if node is None:
            return None
        self.deepsinorder(node.right)
        print(node)
        self.deepsinorder(node.left)
    def presorder(self,node):
        stack=[]
        while node or len(stack)>0:
            while node:
                print(node)
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                node=node.right
    def insorder(self,node):
        stack=[]
        while node or len(stack) >0:
            while node:
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                print(node)
                node=node.right

