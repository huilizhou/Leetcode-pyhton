# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 我的想法
        if not head:
            return
        res = []
        while head:
            res.append(head.val)
            head = head.next
        K = k % len(res)
        res = res[-K:] + res[:-K]

        head = h = ListNode(0)
        for i in res:
            head.next = ListNode(i)
            head = head.next
        return h.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
print(Solution().rotateRight(l1, 2))
