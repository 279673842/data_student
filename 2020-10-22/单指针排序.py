def patition(nums, start, end):
    poivt = nums[start]
    mark = start
    for i in range(start+1,end+1):
        if nums[i] < poivt:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[start] = nums[mark]
    nums[mark] = poivt
    return mark


def singlesort(nums, start, end):
    if start >= end:
        return
    mid = patition(nums, start, end)
    singlesort(nums, start, mid - 1)
    singlesort(nums, mid + 1, end)


nums = [4, 7, 3, 5, 6, 2, 8, 1, 9]
singlesort(nums, 0, len(nums)-1)
print(nums)
