class queue:
    def __init__(self):
        self.data_list=[]
        self.size=0
    def enqueue(self,data):
        self.data_list.append(data)
        index=len(self.data_list)-1
        self.heaifyup(index)
        self.size+=1
    def heaifyup(self,index):
         parents=(index-1)>>1
         while index>0 and self.data_list[index]>self.data_list[parents]:
            self.swap(index,parents)
            index=parents
            parents=(index-1)>>1
    def swap(self, index, parents):
        self.data_list[index],self.data_list[parents]=self.data_list[parents],self.data_list[index]
    def unqueue(self):
        if self.size <= 0:
            raise Exception('空队列')
        self.data_list[0]=self.data_list[-1]
        self.data_list.pop()
        self.heaifydown()
        self.size-=1

    def heaifydown(self):
        index=0
        # children=index
        tail_index=len(self.data_list)-1
        while True:
            children = index
            if 2*index+1 <=tail_index and self.data_list[2*index+1]>self.data_list[children]:
                children=2*index+1
            if 2*index+1 <=tail_index and self.data_list[2*index+1]>self.data_list[children]:
                children=2*index+2
            if children==index:
                break
            self.swap(index,children)
            index=children
if __name__ == '__main__':
    h = queue()
    h.enqueue(3)
    h.enqueue(5)
    h.enqueue(10)
    h.enqueue(2)
    h.enqueue(7)
    h.unqueue()
    print(h.data_list)

