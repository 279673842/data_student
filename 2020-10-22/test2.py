# class Node:
#     def __init__(self):
#         self.data={}
#         self.is_word=False
#     def __repr__(self):
#         return str(self.data)
# class dictrie:
#     def __init__(self):
#         self.root=Node()
#     def insert(self,word):
#         node=self.root
#         for char in word:
#             child=node.data.get(char)
#             if child is None:
#                 node.data[char]=Node()
#             node=node.data[char]
#         node.is_word=True
#     def search(self,word):
#         node = self.root
#         for char in word:
#             node = node.data.get(char)
#             if node is None:
#                 return False
#         return node.is_word
#     def startwith(self,word):
#         node=self.root
#         for char in  word:
#             node=node.data.get(char)
#             if node is None:
#                 return False
#         return True
# class Node:
#     def __init__(self):
#         self.data={}
#         self.is_word=False
#     def __repr__(self):
#         return str(self.data)
# class dictrie:
#     def __init__(self):
#         self.root=Node()
#     def insert(self,word):
#         node=self.root
#         for char in word:
#             child=node.data.get(char)
#             if child is None:
#                 node.data[char]=Node()
#             node=node.data[char]
#         node.is_word=True
#     def search(self,word):
#         node=self.root
#         for char in word:
#             node=node.data.get(char)
#             if not node:
#                 return False
#         return node.is_word
#
#     def startwith(self,word):
#         node=self.root
#         for char in word:
#             node=node.data.get(char)
#             if not node:
#                 return False
#         return True
# if __name__ == '__main__':
#     d=dictrie()
#     d.insert("some")
#     d.insert("something")
#     print(d.root.data)
#     print(d.search("some"))
#     print(d.search("something"))
#     print(d.startwith("some"))

# def partition(nums, start, end):
#     pivot=nums[start]
#     mart=start+1
#     for i in range(start,end):
#         if nums[i]<pivot:
#             mart+=1
#             nums[mart],nums[i]=nums[i],nums[mart]
#     nums[start]=nums[mart]
#     nums[mart]=pivot
#     return mart



def singel(nums,start,end):
    if start>=end:
        return
    mid=partition(nums,start,end)
    singel(nums,start,mid-1)
    singel(nums,mid+1,end)
def partition(nums, start, end):
    piovt=nums[start]
    mart=start
    for i in  range(start+1,end+1):
        if nums[i]<piovt:
            mart+=1
            nums[i],nums[mart]=nums[mart],nums[i]
    nums[start]=nums[mart]
    nums[mart]=piovt
    return mart


def singlesort(nums,start,end):
    if start >= end:
        return
    mid=partition(nums,start,end)
    singlesort(nums,start,mid-1)
    singlesort(nums,mid+1,end)

nums = [4, 7, 3, 5, 6, 2, 8, 1, 9]
singlesort(nums, 0, len(nums)-1)
print(nums)

def countsort(nums):
    if len(nums)<2:
        return  nums
    geart=max(nums)
    new=[0]*(geart+1)
    for i in  nums:
        new[i]+=1
    output=[]
    for i in range(len(new)):
        for j in range(new[i]):
            output.append(i)
    return output
print(countsort([9, 3, 5, 4, 9, 1, 2, 7, 8, 1, 3, 6, 5, 3, 4, 0, 10, 9, 7, 9]))