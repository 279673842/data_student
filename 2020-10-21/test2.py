from typing import List
def merge(left, right):
    result = []
    while left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result

# def merge(left, right):
#     result = []
#     while left and right:
#         if left[0] > right[0]:
#             result.append(right.pop(0))
#         else:
#             result.append(left.pop(0))
#     if left:
#         result.extend(left)
#     if right:
#         result.extend(right)
#     return result


# def mergesort(nums: List):
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums) >> 1
#     left, right = nums[0:mid], nums[mid:]
#     return merge(mergesort(left), mergesort(right))


def mergesort(nums:List):
    if len(nums) < 2:
        return nums
    mid = len(nums) >> 1
    left = nums[0:mid]
    right = nums[mid:]
    return merge(mergesort(left),mergesort(right))


#     result = []
#     while left and right:
#         if left[0] > right[0]:
#             result.append(right.pop(0))
#         else:
#             result.append(left.pop(0))
#     if left:
#         result.append(left)
#     if right:
#         result.append(right)
#     return result
#
#
# def mergesort2(nums:List):
#     if len(nums) < 2:
#         return nums
#     mid = len(nums) >> 1
#     left = nums[0:mid]
#     right = nums[mid:]
#     return merges(mergesort2(left), mergesort2(right))


print(mergesort([2, 3, 1, 5, 7, 2, 3, 1, 8]))
# print(mergesort2([2, 3, 1, 5, 7, 2, 3, 1, 8]))
