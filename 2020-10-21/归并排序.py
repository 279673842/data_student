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

def mergesort(nums: List):
    if len(nums) <= 1:
        return nums
    mid = len(nums) >> 1
    left, right = nums[0:mid], nums[mid:]
    return merge(mergesort(left), mergesort(right))


def mergesort2(nums: List):
    if len(nums) <= 1:
        return nums
    mid = len(nums) >> 1
    left, right = nums[0:mid], nums[mid:]
    return merge2(mergesort(left), mergesort(right))


def merge2(left, right):
    result = []
    start_left = 0
    start_right = 0
    while start_left < len(left) and start_right < len(right):
        if left[start_left] > right[start_right]:
            result.append(right[start_right])
            start_right += 1
        else:
            result.append(left[start_left])
            start_left += 1
    if start_left < len(left):
        result.extend(left[start_left:])
    if start_right < len(right):
        result.extend(right[start_right:])
    return result

print(mergesort([2, 3, 1, 5, 7, 2, 3, 1, 8]))
print(mergesort2([2, 3, 1, 5, 7, 2, 3, 1, 8]))
