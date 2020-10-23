def countsort(nums):
    if len(nums)<2:
        return nums
    max_num=max(nums)
    new=[0]*(max_num+1)
    for i in range(len(new)):
        new[i]=nums.count(i)
    # for i in  nums:
    #     new[i]+=1
    output=[]
    for i in range(max_num+1):
        for j in range(new[i]):
            output.append(i)
    return output


print(countsort([9, 3, 5, 4, 9, 1, 2, 7, 8, 1, 3, 6, 5, 3, 4, 0, 10, 9, 7, 9]))