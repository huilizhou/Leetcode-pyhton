class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "None"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


# import sys

# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))

#         dummy = L1 = ListNode(0)
#         for j in values:
#             dummy.next = ListNode(j)
#             dummy = dummy.next
#         print('L1', L1.next)

#         # dummy = L2 = ListNode(0)
#         # for i in values:
#         #     dummy.next = ListNode(i)
#         #     dummy = dummy.next
#         # print(L2.next)


'''
合并两个有序链表
'''
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))

    dummy = L1 = ListNode(0)
    for j in values:
        dummy.next = ListNode(j)
        dummy = dummy.next
    # print('L1', l1.next)

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    dummy = L2 = ListNode(0)
    for i in values:
        dummy.next = ListNode(i)
        dummy = dummy.next
    # print('L2', l2.next)

    curr = dummy = ListNode(0)
    l1 = L1.next
    l2 = L2.next
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    print(dummy.next)
