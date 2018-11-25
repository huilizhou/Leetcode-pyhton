# 删除链表的倒数第N个节点
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # 首先用两个指针fast,slow 分别指向头结点，然后将其中一个指针向后移动N个位置。
        # 再将两个指针同时往后移动，当fast指针移动到末尾时，slow指针指向的结点即为我们要删除的

        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next
        while first != None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(2)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)
l.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next = ListNode(6)
print(Solution().removeNthFromEnd(l, 1))
