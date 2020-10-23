import random
def bubble(nums):
    count=0
    for i in range(len(nums)-1):
        flag=True
        for j in range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                flag=False
                nums[j],nums[j+1]=nums[j+1],nums[j]
            count += 1
            # print("第%s轮排序结果"%(count),nums)
        if flag:
            break
    return nums
num=[]
for i in range(15):
    num.append(random.randint(1,100))
print(num)
print(bubble(num))