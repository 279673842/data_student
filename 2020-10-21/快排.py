from typing import List

def swap(nums, p, q):
    nums[p], nums[q] = nums[q], nums[p]

def partition(nums, start, end):
    privot = nums[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and nums[p] < privot:
            p += 1
        while p <= q and nums[q] >= privot:
            q -= 1
        if p < q:
            swap(nums, p, q)
    swap(nums, start, q)
    return q

def quicksort(nums: List, start, end):
    if start >= end:
        return
    mid = partition(nums, start, end)
    quicksort(nums, start, mid - 1)
    quicksort(nums, mid + 1, end)


nums = [1, 2, 4, 6, 72, 3, 2, 6]
quicksort(nums, 0, len(nums) - 1)
print(nums)


def quicksort2(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort2(less) + [pivot] + quicksort2(greater)
def quicksort3(array):
    if len(array)<2:
        return  array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i <= pivot]
        greater =[i for i in array[1:] if i >pivot]
        return quicksort3(less) +[pivot] + quicksort3(greater)

def quicksort4(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i <=pivot]
        greater=[i for i in array[1:] if i >pivot]
        return quicksort4(less) +[pivot] + quicksort4(greater)


def partitions(array, start, end):
    pivot=array[start]
    p=start
    q=end
    while p<=q:
        while q<=p and array[p]<pivot:
            p+=1
        while q <= p and array[q] < pivot:
            q -= 1
        if p<q:
            swap(array,p,q)
    return q




def quicksort5(array,start,end):
    if start>=end:
        return
    mid=partitions(array,start,end)
    quicksort5(array,start,mid-1)
    quicksort5(array,mid+1,end)
def quicksort6(array,start,end):
    if start >=end:
        return
    mid=partition(array,start,end)
    quicksort6(array,start,mid-1)
    quicksort6(array,mid+1,end)

def partition2(array,start,end):
    pivot=array[0]
    p=start
    q=end
    while p<=q:
        while p<=q and array[p]<pivot:
            p+=1
        while p<=q and array[q]<pivot:
            q-=1
        if p<q:
            swap(array,p,q)
    return  p

nums = [1, 2, 4, 6, 72, 3, 2, 6]
# quicksort2(nums)
# print(quicksort2(nums))
# print(quicksort3(nums))
# # print(nums)
# quicksort5(nums,0,len(nums)-1)
# print(nums)
quicksort6(nums,0,len(nums)-1)
print(nums)