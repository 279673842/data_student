class Node:
    def __init__(self):
        self.data={}#创建一个字典节点
        self.is_word=False#节点的单词结束标识
    def __repr__(self):#打印函数
        return f"{self.data}"
class dictrie:#字典树类
    def __init__(self):#字典树属性,开始节点
        self.root=Node()#根节点

    def insert(self,word):#插入函数
        node=self.root#找到开始根节点
        for char in word:#遍历这个字符串
            child=node.data.get(char)#每层查找这个字符是否存在
            if child is None:#如果这个字符不存在
               node.data[char]= Node()#创建这个字符节点
            node=node.data[char]#节点下移
        node.is_word=True#单词完成之后的,结束标识
    def search(self,word):#完整查找
        node = self.root#找到根节点
        for char in word:#遍历查找的单词
            node= node.data.get(char)#节点下移
            if not node:#如果这个查找的节点不存在
                return False#直接返回没有
        return node.is_word#如果词查完了,但是没有结束标识,也返回错误
    def startwith(self,word):#存在查找
        node=self.root#找到根节点
        for char in word:#遍历查找的单词
            node=node.data.get(char)#节点下移
            if not node:#如果这个查找的节点不存在
                return False#直接返回没有
        return True#只要存在这个单词的内容既返回正确

if __name__ == '__main__':
    d=dictrie()
    d.insert("some")
    d.insert("something")
    print(d.root.data)
    print(d.search("some"))
    print(d.search("something"))
    print(d.startwith("somet"))