class queue:
    def __init__(self):
        self.size = 0
        self.data_list = []

    def swap(self, index, parent):
        self.data_list[index], self.data_list[parent] = self.data_list[parent], self.data_list[index]

    def enqueue(self, data):
        self.data_list.append(data)
        self.heaify()
        self.size += 1

    def heaify(self):
        index = len(self.data_list) - 1
        parent = (index - 1) >> 1
        while index > 0 and self.data_list[index] > self.data_list[parent]:
            self.swap(index, parent)
            index = parent
            parent = (index) >> 1

    def dequeue(self):
        self.data_list[0] = self.data_list[-1]
        self.data_list.pop()
        self.heaifydown()
        self.size -= 1

    def heaifydown(self):
        index = 0
        tail_index = len(self.data_list) - 1
        while True:
            max_index = index
            if 2 * index + \
                    1 <= tail_index and self.data_list[2 * index + 1] > self.data_list[max_index]:
                max_index = 2 * index + 1
            if 2 * index + \
                    2 <= tail_index and self.data_list[2 * index + 2] > self.data_list[max_index]:
                max_index = 2 * index + 1
            if index == max_index:
                break
            self.swap(index, max_index)
            index = max_index


if __name__ == '__main__':
    h = queue()
    h.enqueue(3)
    h.enqueue(5)
    h.enqueue(10)
    h.enqueue(2)
    h.enqueue(7)
    h.dequeue()
    print(h.data_list)
