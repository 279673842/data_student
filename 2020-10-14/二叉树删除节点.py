from pprint import pformat#导入打印树的pformat包

class Node:#建立节点
    def __init__(self, data, parent):#传入节点参数属性和,父节点指向(根节点父节点指向为None)
        self.data = data#节点参数属性
        self.parent = parent#父节点指向
        self.left = None#左子树指向
        self.right = None#右子树指向

    def __repr__(self):#打印函数
        return pformat({"%s" % (self.data): (self.left, self.right)}, indent=1)

class dinarytree:#建立二叉树类
    def __init__(self):
        self.root = None#根节点

    def __repr__(self):#打印函数
        return str(self.root)
    def insert(self, data):#插入函数,传入需要插入的值
        node = Node(data, None)#把值建立一个节点
        if self.root is None:#如果根节点是空,则把新加入的节点作为根节点
            self.root = node
        else:
            temp = self.root#如果不为空,找到根节点的位置
            while temp:#从根节点向下循环找空位置
                if data <= temp.data:#比较插入的值,如果小于temp的值,则在temp的节点左子树中寻找空位置插入
                    if temp.left:#如果temp的左子树不为空
                        temp = temp.left#在左子树向下寻找
                    else:
                        temp.left = node#如果temp的左子树为空,在temp的左边孩子插入
                        break#插入完成,退出循环
                elif data > temp.data:#如果大于temp的值,则在temp的节点右子树中寻找空位置插入
                    if temp.right:#如果右子树已存在
                        temp = temp.right#在右孩子中向下寻找
                    else:
                        temp.right = node#如果temp的右子树为空,在temp的右边孩子插入
                        break#插入完成,退出循环
                node.parent = temp#新插入节点的父节点指向temp
    # ======二叉查询树查找节点==========
    # def search(self, val):
    #     if self.root is None:
    #         raise IndexError(" empty tree")
    #     else:
    #         temp = self.root
    #         while temp and temp.data != val:
    #             if val<temp.data  :
    #                 temp = temp.left
    #             elif val> temp.data:
    #                 temp = temp.right
    #     return temp

    def search(self, val):
        if self.root is None:
            raise IndexError(" empty tree")
        else:
            node = self.root
            while node and node.data != val:
                if val < node.data:
                    node = node.left
                elif val > node.data:
                    node = node.right
            # print(node)
            return node

    def remove(self, value):
        node = self.search(value)
        if node is not None:
            if node.right is None and node.left is None:
                self.__reassion_node(node, None)
            elif node.right is None:
                self.__reassion_node(node, node.left)
            elif node.left is None:
                self.__reassion_node(node, node.right)
            else:
                temp = self.get_max(node.left)
                self.remove(temp.data)
                node.data = temp.data
        else:
            raise IndexError("empty")
    def is_right(self, node):
        return node == node.parent.right
    def __reassion_node(self, node, children):
        if children is not None:
            children.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = children
            else:
                node.parent.left = children
        else:
            self.root = node

    def get_max(self, node):
        if self.is_right(node):
            while node.left:
                node = node.left
            return node
        else:
            while node.right:
                node = node.right
            return node


if __name__ == '__main__':
    t = dinarytree()
    # t.add(1)
    # t.add(2)
    # t.add(3)
    # t.add(4)
    # t.add(15)
    t.insert(4)
    t.insert(2)
    t.insert(1)
    t.insert(3)
    t.insert(15)
    t.insert(14)
    t.insert(16)
    t.insert(4)
    t.search(4)
    print(t.search(14))
    print(t)
    t.remove(14)
    print(t)
