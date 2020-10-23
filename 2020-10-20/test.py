# 选择排序
# def bubble(nums):
#     nums=[]
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[j]<nums[i]:
#                 index=j
#         if i != index :
#             nums[i],nums[index]=nums[index],nums[i]
#     return nums

# 冒泡排序
# def bubble(nums):
#     nums=[]
#     for i in range(len(nums)-1):
#         flag=True
#         for j in range(len(nums)-1-i):
#             if nums[j]<nums[j+1]:
#                 nums[i],nums[j]=nums[j],nums[i]
#                 flag=False
#         if flag:
#             break
#     return nums

