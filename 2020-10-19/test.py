class dinarytree:
    def __init__(self):
        self.root=None
    def remove(self,data):
        node=self.search(data)
        if node.left is None and node.right is None:
            self._reassgin(node,None)
        elif node.left is None :
            self._reassgin(node,node.right)
        elif node.right is None:
            self._reassgin(node,node.left)
        else:
            temp=self.get_max(node.left)
            self.remove(temp.data)
            node.data=temp.data
    def search(self, data):
        pass

    def _reassgin(self, node, children):
        if children is not None:
            children.parent=node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right=children
            else:
                node.parent.left = children
        else:
            self.root=node
    def get_max(self, node):
        if node is None:
            node=self.root
        while node.right:
            node=node.right

    def is_right(self, node):
        return node==node.parent.right

    # 递归
    def preorder(self,node):
        if node is None:
            return None
        print(node)
        self.preorder(node.right)
        self.preorder(node.left)
    def inorder(self,node):
        if node is None:
            return None
        self.preorder(node.right)
        print(node)
        self.preorder(node.left)

    # 遍历
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
    def postorder(self,node):
        stack=[node]
        stack2=[]
        while node or len(stack)>0:
            node=stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            stack.append(node)
        while stack2:
            print(stack2.pop())