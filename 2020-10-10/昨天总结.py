# 26.
# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

from typing import List


class delmm:
    def dels(self, nums: List):
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1
# 80. 删除排序数组中的重复项 II
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。


class del_two:
    def dels(self, nums):
        fast = 1
        slow = 0
        count = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                count += 1
                fast += 1
                if count == 2:
                    slow += 1
                    nums[slow] = nums[fast]
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1


# 27.
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。


class delmn:
    def dels(self, nums: List, val):
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1


# 283. 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。


class delmq:
    def dels(self, nums: List):
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return slow + 1


# 链表做栈
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)


class stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("错误")
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.size -= 1
# 列表做栈


class stack2:
    def __init__(self):
        self.top = []
        self.size = 0

    def push2(self, data):
        self.top.append(data)
        self.size += 1

    def pop(self):
        if self.top:
            temp = self.top.pop(self.size - 1)
            self.size -= 1
        else:
            raise IndexError("KONG")
        return temp

    def output(self):
        for i in range(self.size - 1, -1, -1):
            print(self.top[i])
        return self.top

    def peek(self):
        if self.top:
            return self.top[-1]
        else:
            raise IndexError("KONG")
