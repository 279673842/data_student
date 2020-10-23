from pprint import pformat


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        return pformat({"%s" % (self.data): (self.left, self.right)}, indent=1)


class Dinarysearchtree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def insert(self, data):
        node = Node(data, None)
        if self.root is None:
            self.root = node
        else:
            temp = self.root
            while temp:
                if data >= temp.data:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = node
                        break
                elif data < temp.data:
                    if temp.left:
                        temp = temp.left
                    else:
                        temp.left = node
                        break
                node.parent = temp

    def search(self, data):
        if self.root is None:
            raise IndexError("empty")
        else:
            temp = self.root
            while temp and temp.data != data:
                if data > temp.data:
                    temp = temp.right
                elif data < temp.data:
                    temp = temp.left
            return temp

    def remove(self, data):
        node = self.search(data)
        if node is not None:
            if node.left is None and node.right is None:
                self._reassign(node, None)
            elif node.left is not None:
                self._reassign(node, node.left)
            elif node.right is not None:
                self._reassign(node, node.right)
            else:
                temp = self.get_max(node)
                self.remove(temp.data)
                node.data = temp.data

    def _reassign(self, node, childern):
        if childern is not None:
            childern.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = childern
            else:
                node.parent.left = childern
        else:
            self.root = node


    def get_max(self, node):
        if self.is_right(node):
            while node.left:
                node = node.left
        else:
            while node.right:
                node = node.right
        return node

    def is_right(self, node):
        return node == node.parent.right


if __name__ == '__main__':
    t = Dinarysearchtree()
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
