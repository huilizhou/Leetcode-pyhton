# 链表的中间结点
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "None"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 我的想法
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[len(res) // 2:]

        # 人家的解法，类似
        # length = 0
        # p = head
        # while p is not None:
        #     p = p.next
        #     length += 1
        # middle = length // 2

        # p = head
        # for _ in range(middle):
        #     p = p.next
        # return p


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
print(Solution().middleNode(l1))
