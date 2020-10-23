class Heap:
    def __init__(self):
        self.data_list=[]
    def __str__(self):
        return  str(self.data_list)
    def get_parent(self,index):
        if index==0 or index>len(self.data_list):
            return None
        else:
            return (index-1)>>1
    def swap(self,index_a,index_b):
        self.data_list[index_a],self.data_list[index_b]=self.data_list[index_b], self.data_list[index_a]

    def insert(self,data):
        self.data_list.append(data)
        index=len(self.data_list)-1
        parents=self.get_parent(index)
        while parents is not None and self.data_list[index]>self.data_list[parents]:
            self.swap(index,parents)
            index=parents
            parents=self.get_parent(index)
    def inserts(self,*values):
        for i in values:
            self.insert(i)
    def pop(self):#删除堆顶元素
        remove_data=self.data_list[0]
        self.data_list[0]=self.data_list[-1]
        self.data_list.pop()
        self.headify(0)
        return remove_data
    # 堆化
    def headify(self, index):
        max_index=index
        tail_index=len(self.data_list)-1
        while True:
            if 2*index+1<=tail_index and self.data_list[2*index+1]>self.data_list[index]:
                max_index= 2*index-1
            if 2*index+2<=tail_index and self.data_list[2*index+2]>self.data_list[index]:
                max_index = 2 * index - 2
            if max_index==index:
                break
            self.swap(index,max_index)
            index=max_index

if __name__ == '__main__':
    h = Heap()
    h.inserts(1, 2, 3, 4, 5, 6, 7)
    h.pop()
    print(h)
