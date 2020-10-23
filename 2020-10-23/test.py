# def partition(nums, start, end):#单指针
#     pivot=nums[start]
#     mark=start
#     for i in range(start+1,end+1):
#         if nums[i]<pivot:
#             mark+=1
#             nums[mark],nums[i]=nums[i],nums[mark]
#     nums[start]=nums[mark]
#     nums[mark]=pivot
#     return mark


# def partition(nums, start, end):#快排
#     piovt=nums[start]
#     p=start+1
#     q=end
#     while p<=q:
#         while p<=q and nums[p]<piovt:
#             p+=1
#         while p<=q and nums[q]>=piovt:
#             q-=1
#         if p<q:
#             nums[p],nums[q]=nums[q],nums[p]
#     nums[q],nums[start]=nums[start],nums[q]
#     return q

# def singlesort(nums,start,end):
#     if start >=end:
#         return
#     mid=partition(nums,start,end)
#     singlesort(nums,start,mid-1)
#     singlesort(nums,mid+1,end)


# nums = [4, 7, 3, 5, 6, 2, 8, 1, 9]
# singlesort(nums, 0, len(nums)-1)
# print(nums)


class Node:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def __repr__(self):
        return str(self.data)


class dictrie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for i in word:
            child = node.data.get(i)
            if child is None:
                node.data[i] = Node()
            node = node.data[i]
        node.is_word = True

    def search(self, word):
        node = self.root
        for i in word:
            node = node.data.get(i)
            if node is None:
                return False
        return node.is_word

    def startwith(self, word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if node is None:
                return False
        return True


if __name__ == '__main__':
    d = dictrie()
    d.insert("some")
    d.insert("something")
    print(d.root.data)
    print(d.search("some"))
    print(d.search("something"))
    print(d.startwith("somet"))


def countsort(nums):
    if len(nums) < 2:
        return nums
    great = max(nums)
    new = [0] * (great + 1)
    for i in nums:
        new[i] += 1
    output = []
    for i in range(great + 1):
        for j in range(new[i]):
            output.append(i)
    return output


print(countsort([9, 3, 5, 4, 9, 1, 2, 7, 8, 1, 3, 6, 5, 3, 4, 0, 10, 9, 7, 9]))


def quicksort(nums):#快排1
    if len(nums) < 2:
        return nums
    piovt = nums[0]
    less = [i for i in nums[1:] if i < piovt]
    greater = [i for i in nums[1:] if i > piovt]
    return quicksort(less) + [piovt] + quicksort(greater)


nums = [4, 7, 3, 5, 6, 2, 8, 1, 9]
print(quicksort(nums))


def partition(nums, start, end):#快排2
    piovt = nums[start]
    p = start+1
    q = end
    while p <= q:
        while p <= q and nums[p] < piovt:
            p += 1
        while p <= q and nums[q] >= piovt:
            q -= 1
        if p < q:
            nums[p], nums[q] = nums[q], nums[p]
    nums[start], nums[q] = nums[q], nums[start]
    return q

def quicksort2(nums, start, end):
    if start >= end:
        return
    mid = partition(nums, start, end)
    quicksort2(nums, start, mid - 1)
    quicksort2(nums, mid + 1, end)


nums = [1, 2, 4, 6, 72, 3, 2, 6]
quicksort2(nums, 0, len(nums) - 1)
print(nums)
