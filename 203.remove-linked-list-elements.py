# Definition for singly - linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(float('-inf'))
        dummy.next = head

        ret, current = dummy, dummy.next

        while current:
            if current.val == val:
                ret.next = current.next
            else:
                ret = current
            current = current.next

        return dummy.next

        # t = ListNode(None)
        # t.next = head
        # a = t
        # while a.next:
        #     if a.next.val == val:
        #         a.next = a.next.next
        #     else:
        #         a = a.next
        # return t.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(6)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)
l.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next = ListNode(6)

print(Solution().removeElements(l, 6))
