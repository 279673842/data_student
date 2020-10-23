# from typing import  List
# # # class Solution:
# # #     def threeSum(self, nums: List[int]) -> List[List[int]]:
# # #         # nums.sort()
# # #         a=[]
# # #         for i in nums:
# # #             for j in nums:
# # #                 for k in nums:
# # #                     if i != j != k:
# # #                         if i+j+k==0:
# # #                             while [i,j,k] not in a:
# # #                                 a.append([i,j,k].sort())
# # #         return a
# a=[3,2,3]
# print(a[-1])
# a.remove(3)
# print(a)
# print(a.index(3)+1)
# from typing import  List
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        # fast=1
#         # slow=0
#
#         # for i in range(len(nums)):
#         #     for j in range(i+1,len(nums)):
#         #         if nums[i] + nums[j]== target:
#         #             return  i,j
#         # dic={}
#         # for i in range(len(nums)):
#         #     if target-nums[i] in dic:
#         #         # num=nums[i]
#         #         return dic[target-nums[i]],i
#         #     else:
#         #         dic[nums[i]]=i
#         num = []
#         nu = []
#         for i in nums:
#             num.append(i)
#             nu.append(i)
#         nums.sort()
#         a = 0
#         b = -1
#         # for a in nums[1:] and b in nums[-1:] :
#         while a < len(nums) and b < len(nums):
#
#             if nums[a] + nums[b] == target:
#                 # return nums[a],nums[b]
#                 break
#             elif nums[a] + nums[b] > target:
#                 b -= 1
#                 continue
#             elif nums[a] + nums[b] < target:
#                 a += 1
#                 continue
#         if nums[a]<0 and nums[b]<0:
#             nums[a], nums[b]= nums[b],nums[a]
#         m = num.index(nums[a])
#         if a<len(nums)+b:
#             nu.remove(nums[a])
#             n = nu.index(nums[b]) + 1
#         else:
#             n = num[num.index(nums[a]):].index(nums[b])
#         return m,n,nums[a],nums[b],nu,len(nums)+b,a,num
# aa=Solution()
# print(aa.twoSum([5,75,25],100))
# # print(aa.twoSum([3,2,3],6))
# p=[3, 2, 3]
# p.remove(3)
# print(p)



from typing import  List
# def Twosum(nums:List,target):
#     head=0
#     end=len(nums)-1
#     while head < end:
#         if nums[head]+nums[end]==target:
#             print(nums[head],nums[end])
#             head+=1
#             end-=1
#         else:
#             if nums[head]+nums[end] > target:
#                 end-=1
#             else:
#                 head+=1
#
# print(Twosum([1,2,3,4,5,6,7,8,9,10],10))


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dic={}
#         for i in  range(len(nums)):
#             if target-nums[i] in dic:
#                 return dic[target-nums[i]],i
#             else:
#                 dic[nums[i]]=i
# ===============================================二叉树
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def __repr__(self):
#         return  f"{self.data}"
#
# class Binarytree:
#     def __init__(self):
#         self.root=None
#     def add(self,data):
#         node=Node(data)
#         if self.root is None :
#             self.root=node
#         else:
#             temp=[self.root]
#             while True:
#                 temp_pop=temp.pop(0)
#                 if temp_pop.left is None:
#                     temp_pop.left=node
#                     return
#                 elif temp_pop.right is None:
#                     temp_pop.right=node
#                     return
#                 else:
#                     temp.append(temp_pop.left)
#                     temp.append(temp_pop.right)
#     def gets(self,data):
#         if self.root.data==data:
#             print("根节点没有父节点")
#         temp=[self.root]
#         while temp:
#             pop_node=temp.pop(0)
#             if pop_node.left:
#                 if pop_node.left.data==data:
#                     print(pop_node.left)
#                     temp.append(pop_node.left)
#             elif pop_node.right:
#                 if pop_node.right.data==data:
#                     print(pop_node.right)
#                     temp.append(pop_node.right)
#             return None
# ============================================二叉排序树
# from pprint import pformat
# class Node:
#     def __init__(self, data,parent):
#         self.data = data
#         self.parent=parent
#         self.left = None
#         self.right = None
#     def __repr__(self):
#         # return f"{self.data}"
#         return pformat({"%s"%(self.data):(self.left,self.right)},indent=1)
# class Binarytree:
#     def __init__(self):
#         self.root = None
#     def __repr__(self):
#         return str(self.root)
#         # return pformat({"%s"%(self.data):(self.left,self.right)},indent=1)
#     def isempty(self):
#         if self.root:
#             return True
#         else:
#             return False
#
#     def insert(self,vall):
#         node=Node(vall,None)
#         if self.root is None:
#             self.root=node
#         else:
#             parent_node=self.root
#             while parent_node:
#                 if vall< parent_node.data:
#                     if parent_node.left :
#                         parent_node = parent_node.left
#                     else:
#                         parent_node.left = node
#                         break
#                 elif vall>parent_node.data:
#                     if parent_node.right:
#                         parent_node=parent_node.right
#                     else:
#                         parent_node.right=node
#                         break
from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data=data
        self.parent=parent
        self.left=None
        self.right=None
    def __repr__(self):
        # return f"{self.data}"
        return pformat({"%s" % (self.data): (self.left, self.right)}, indent=1)
class Binarysorttree:
    def __init__(self):
        self.root=None
    def __repr__(self):
        return str(self.root)
    def isempty(self):
        if self.root:
            return True
        else:
            return False
    def insert(self,val):
        node=Node(val,None)
        if self.root is None:
            self.root=node
        else:
            parent_node=self.root
            while parent_node:
                if val < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left=node
                        break
                    else:
                        parent_node=parent_node.left

                elif val >=parent_node.data:
                    if parent_node.right is None:
                        parent_node.right=node
                        break
                    else:
                        parent_node = parent_node.right

    def search(self,val):
        if  self.root is None:
            raise IndexError(" empty tree")
        else:
            node=self.root
            while node and node.data != val :
                if val < node.data:
                    node = node.left
                elif val > node.data:
                    node = node.right
            # print(node)
            return node

if __name__ == '__main__':
    t=Binarysorttree()
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
    # t.insert(4)
    t.search(4)
    print(t.search(14))
    print(t)

# from pprint import pformat
# class Node:
#     def __init__(self,data,parent):
#         self.data=data
#         self.parent=parent
#         self.right=None
#         self.left=None
#     def __repr__(self):
#         # return f"{self.data}"
#         return pformat({"%s" %(self.parent):(self.left,self.right)},indent=1)
#
# class BST:
#     def __init__(self):
#         self.root=None
#     def __repr__(self):
#         return set(self.root)
#     def isempty(self):
#         if self.root is None:
#             return True
#         else:
#             return False
#     def insert(self,val):
#         node=Node(val,None)
#         if self.isempty():
#             self.root=node
#         else:
#             temp=self.root
#             while True:
#                 if val < temp:
#                     if temp.left is None:
#                         temp.left=node
#                         break
#                     else:
#                         temp=temp.left
#                 elif val > temp:
#                     if temp.right is None:
#                         temp.right = node
#                         break
#                     else:
#                         temp = temp.right
#     def search(self,val):
#         if self.isempty():
#             raise IndexError("empty tree,search where")
#         else:
#             temp = self.root
#             while temp and temp.left:
#                 if val < temp.data:
#                         temp=temp.left
#                 elif val >temp.data:
#                         temp=temp.right
#                 return temp
#
# class Node1:
#     def __init__(self,data,parent):
#         self.data=data
#         self.parent=parent
#         self.right=None
#         self.left=None


