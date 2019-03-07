# 删除排序链表中的重复元素
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # # 直接法
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(2)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)
l.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next = ListNode(6)

print(Solution().deleteDuplicates(l))
