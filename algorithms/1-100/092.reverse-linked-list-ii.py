# 反转链表II
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # # 我的解法
        # if not head:
        #     return
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # res = res[:m - 1] + list(reversed(res[m - 1:n])) + res[n:]
        # return res

        # 人家的解法
        if head == None or head.next == None:
            return head
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        q = dummy.next
        for _ in range(1, m):
            p = p.next
            q = q.next

        for _ in range(m, n):
            r = p.next
            p.next = q.next
            q.next = p.next.next
            p.next.next = r

        return dummy.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)


print(Solution().reverseBetween(l, 2, 4))
