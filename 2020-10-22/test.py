# 归并
def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result


def mergesort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) >> 1
    left = nums[0:mid]
    right = nums[mid:]
    return merge(mergesort(left), mergesort(right))


def merge3(left, right):
    res = []
    i, j = 0, 0
    while left and right:
        if left[i] < right[j]:
            res.append(left.pop(i))
        else:
            res.append(right.pop(j))
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res
# 快排

def quicksort(nums):
    if len(nums) < 2:
        return nums
    else:
        piovt = nums[0]
        less = [i for i in nums[1:] if i < piovt]
        greater = [i for i in nums[1:] if i >= piovt]
        return quicksort(less) + [piovt] + quicksort(greater)


def merge2(nums, start, end):
    piovt = nums[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and nums[p] < piovt:
            p += 1
        while p <= q and nums[q] >= piovt:
            q -= 1
        if p < q:
            nums[q], nums[p] = nums[p], nums[q]
    nums[q], nums[start] = nums[start], nums[q]
    return q


def quicksort2(nums, start, end):
    if start >= end:
        return
    mid = merge2(nums, start, end)
    quicksort2(nums, start, mid-1)
    quicksort2(nums, mid+1, end)


print(quicksort([4, 7, 3, 5, 6, 2, 3]))
print(mergesort([4, 7, 3, 5, 6, 2, 3]))
nums = [4, 7, 3, 5, 6, 2, 3]
quicksort2(nums, 0, len(nums) - 1)
print(nums)
