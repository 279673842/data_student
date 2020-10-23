from pprint import  pformat
class Node:
    def __init__(self,data,parent):
        self.data=data
        self.parent=parent
        self.left=None
        self.right=None

    def __repr__(self):
        if self.left is not None and self.right is not None:
            return f'{self.data}'
        return pformat({"%s"%(self.data):(self.left,self.right)},indent=1)

class binarysearchtree:
    def __init__(self):
        self.root=None
    def __str__(self):
        return  str(self.root)
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
                elif data<temp.data:
                    if temp.left is None:
                        temp.left=node
                        break
                    else:
                        temp=temp.left
            node.parent=temp
    def search(self,data):
        if self.root is None:
            raise IndexError("empty")
        else:
            temp=self.root
            while temp and temp.data != data:
                if data>temp.data:
                    temp=temp.right
                elif data<temp.leftL:
                    temp=temp.left
            return temp
    def remove(self,data):
        node=self.search(data)
        if node.left is None and node.right is None:
            self._reassign(node,None)
        elif node.left is None:
            self._reassign(node, node.right)
        elif node.right is None:
            self._reassign(node,node.left)
        else:
            temp=self.get_max(node.left)
            self.remove(temp.data)
            node.data=temp.data


    def _reassign(self, node, children):
        if children is not None:
            children.parent=node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right=children
            else:
                node.parent.left=children
        else:
            self.root=node

    def get_max(self, node):
        if node is None:
            node=self.root
        while node.right:
            node=node.right

    def is_right(self,node):
        return node==node.parent.right

    # 前序
    def preorder(self,node):
        if node is None:
            return None
        print(node)
        self.preorder(node.right)
        self.preorder(node.left)
    def inorder(self,node):
        if node is None:
            return None
        self.inorder(node.right)
        print(node)
        self.inorder(node.left)
    def preorder2(self,node):
        stack=[]
        while node or len(stack)>0:
            while node:
                print(node)
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                node=node.right
    def preorder3(self,node):
        stack=[node]
        while len(stack):
            print(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node=stack.pop()

    def inorder2(self,node):
        stack=[]
        while node or len(stack)>0:
            while node:
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                print(node)
                node=node.right
    # 后序遍历
    def postorder(self,node):
        stack1=[node]
        stack2=[]
        while len(stack1):
            node=stack1.pop()
            if node.right:
                stack1.append(node.right)
            if node.left:
                stack1.append(node.left)

            stack2.append(node)
        while stack2:
            print(stack2.pop())
    #层序遍历
    def sequence(self,node):
        stack=[node]
        while len(stack)>0:
            node=stack.pop(0)
            print(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    # 层序
    def sequence2(self,node):
        stack=[node]
        while len(stack)>0:
            node=stack.pop(0)
            print(node)
            if node.left:
                stack.pop(node.left)
            if node.right:
                stack.append(node.right)

    def postorder2(self,node):
        stack=[node]
        stack2=[]
        while len(stack)>0:
            node=stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            stack2.append(node)
        while stack2:
            print(stack2.pop())
