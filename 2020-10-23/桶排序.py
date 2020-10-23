nums=[4.5,0.84,3.25,2.18,0.5]
def bucketsort(nums):
    less=min(nums)#最小值
    greater=max(nums)#最大值
    qu=(greater-less)/(len(nums)-1)#区间值
    bucket_num=len(nums)#桶数
    # 创建桶空间
    new=[]
    for i in range(bucket_num):
        new.append([])
    # 二维列表
    for j in range(bucket_num):
        for i in nums:
            if i>=less+qu*j and i <less+qu*(j+1):
                new[j].append(i)
        new[j].sort()
    # 输出
    sort_nums=[]
    for sub in new:
        for item in sub:
            sort_nums.append(item)
    return sort_nums

def bucketsort2(nums):
    greater=max(nums)#最大值
    less=min(nums)#最小值
    diff=greater-less#差
    bucket_num=len(nums)#桶数量
    # 初始化桶,创建桶
    new=[]
    for i in range(bucket_num):
        new.append([])
    # 定位元素属于哪个桶
    for i in range(bucket_num):
        num=int((nums[i]-less)*(bucket_num-1)/diff)
        bucket=new[num]
        bucket.append(nums[i])
    #每个桶排序
    for i in range(bucket_num):
        new[i].sort()
    # 输出
    sort_nums=[]
    for sub in new:
        for item in sub:
            sort_nums.append(item)
    return sort_nums
print(bucketsort(nums))
print(bucketsort2(nums))
