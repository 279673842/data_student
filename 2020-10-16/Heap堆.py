class Heap:  # 堆的创建
    # print(bin(87))
    def __init__(self):#属性函数
        self.data_list = []

    def __repr__(self):#打印函数
        return str(self.data_list)

    def get_parent_index(self, index):#获取父下标的函数
        if index == 0 or index > len(self.data_list)-1 :
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):#交换两个数
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):  # 堆插入函数
        self.data_list.append(data)#堆末尾加入值
        index = len(self.data_list) - 1#新加值的下标
        parents = self.get_parent_index(index)#新加值的父节点下标
        while parents is not None and self.data_list[index] > self.data_list[parents]:
            #父节点可以是根  和父节点的值小于新加值
            self.swap(index, parents) #交换两个值
            index = parents#父节点的下标给这个节点(循环下一个)
            parents = self.get_parent_index(index)#
    def inserts(self, *values):  # 多数循环插入
        for i in values:
            self.insert(i)
    def pop(self):#删除堆顶元素
        removedata=self.data_list[0]
        self.data_list[0]=self.data_list[-1]
        self.data_list.pop()
        self.headify(0)
        return removedata
    # 堆化
    def headify(self, index):
        max_index=index
        tail_index=len(self.data_list)-1
        while True:
            if 2* index +1 <=tail_index and self.data_list[2* index +1 ] > self.data_list[index]:
                max_index=2* index +1
            if 2* index +2 <=tail_index and self.data_list[2* index +2 ] > self.data_list[index]:
                max_index = 2 * index + 2
            if max_index ==index:
                break
            self.swap(max_index,index)
            index=max_index


if __name__ == '__main__':
    h = Heap()
    h.inserts(1, 2, 3, 4, 5, 6, 7)
    h.pop()
    print(h)
