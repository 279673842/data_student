# 重复元素
def remove(nums):
    fast=1
    slow=0
    while fast<len(nums):
        if nums[fast]==nums[slow]:
            fast+=1
        else:
            slow += 1
            nums[slow]=nums[fast]
            fast+=1
    return nums[0:slow+1]
# 删除两个以上的重复元素
def remove2(nums):
    fast=1
    slow=0
    count=1
    while fast<len(nums):
        if nums[fast]==nums[slow]:
            fast+=1
            count+=1
            if count ==2:
                slow+=1
                nums[slow] = nums[fast]
        else:
            slow += 1
            nums[slow]=nums[fast]
            count=1
            fast+=1

# 删除零
def movezeo(nums):
    fast=0
    slow=0
    while fast<len(nums):
        if nums[fast]==0:
            fast+=1
        else:
            nums[slow]=nums[fast]
            slow+=1
            fast+=1
    return nums[0,slow+1]
