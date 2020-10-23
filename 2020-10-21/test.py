class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"
# class link:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     # 链表翻转
#     def revers(self):
#         berfor=None
#         curr=self.head
#         # after=self.head.next
#         while curr:
#             after=curr.next
#             curr.next=berfor
#             berfor=curr
#             curr=after
#         self.head=berfor

# def revers(nums):
#     temp=[]
#     for i in range(nums,-1,-1):
#         temp.append(nums[i])
# 数组翻转
# def reverse(nums):
#     if len(nums) < 2:
#         return nums
#     start=0
#     end=len(nums)-1
#     while start<end:
#         nums[start],nums[end]=nums[end],nums[start]
#         start+=1
#         end-=1
#     return nums
# print(reverse([3, 2, 1, 4, 2, 1, 2]))


def change(head: Node):
    dummy = Node(0)
    curr = head
    pre = dummy
    # after=curr.next
    while curr :
        after = curr.next
        curr.next = after.next
        after.next = curr
        pre.next = after
        pre = curr
        curr = curr.next
        # after=
    return dummy.next
def output(node):
    curcor=node
    strs=""
    while curcor:
        strs+=f"-->{curcor.data}"
        curcor=curcor.next
    return strs+"end"
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = None
    print(output(change(node1)))


def threenumbersum(nums):
    nums.sort()
    mm = []
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        if nums[i] == nums[i - 1]:
            continue
        while j < k:
            sums = nums[i] + nums[j] + nums[k]
            if sums == 0:
                mm.append([nums[i] , nums[j] , nums[k]])
                j += 1
                k -= 1
            elif sums > 0:
                k -= 1
                while nums[k]==nums[k-1]:
                    k-=1
            elif sums < 0:
                j += 1
                while nums[j]==nums[j-1]:
                    j+=1
    return mm


print(threenumbersum([1, 2, 3, -3, 2, 2, -4]))
# -4, -3, 1, 2, 2, 2, 3
