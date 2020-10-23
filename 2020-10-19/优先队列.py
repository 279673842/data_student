class queue:
    def __init__(self):
        self.data_list=[]
        self.size=0
    def __str__(self):
        return str(self.data_list)
    def get_parent(self,index):
        if index ==0 or index >len(self.data_list)-1:
            return None
        return (index-1)>>1
    def enqueue(self,data):
        self.data_list.append(data)
        self.heaifyup()
        self.size +=1
    def heaifyup(self):
        index=len(self.data_list)-1
        parents=self.get_parent(index)
        while parents is not None and self.data_list[index]>self.data_list[parents]:
            self.swap(index,parents)
            index=parents
            parents=self.get_parent(index)
    def headifyup2(self):
        children=len(self.data_list)-1
        parent=(children-1)>>1
        while children>0 and self.data_list[children] > self.data_list[parent]:
            self.swap(children, parent)
            children = parent
            parent = (children-1)>>1
    def unqueue(self):
        self.data_list[0]=self.data_list[-1]
        self.data_list.pop()
        self.headifydown(0)
        self.size-=1
    def headifydown(self,index):
        max_index=index
        tail_index=len(self.data_list)-1
        while True:
            if 2 * index + 1 <= tail_index and self.data_list[2 * index + 1] > self.data_list[max_index]:
                max_index = 2 * index + 1
            if 2 * index + 2 <= tail_index and self.data_list[2 * index + 2] > self.data_list[max_index]:
                max_index = 2 * index + 2
            if max_index == index:
                break
            self.swap(max_index, index)
            index = max_index
    def swap(self, index, parents):
        self.data_list[index],self.data_list[parents]=self.data_list[parents],self.data_list[index]

if __name__ == '__main__':
    h = queue()
    h.enqueue(3)
    h.enqueue(5)
    h.enqueue(10)
    h.enqueue(2)
    h.enqueue(7)
    h.unqueue()
    print(h)
