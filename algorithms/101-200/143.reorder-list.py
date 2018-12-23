# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # 人家的解法
        if head == None or head.next == None:
            return

        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            fast, slow, prev = fast.next.next, slow.next, slow
        current, prev.next, prev = slow, None, None

        while current != None:
            current.next, prev, current = prev, current, current.next

        l1, l2 = head, prev
        dummy = ListNode(0)
        current = dummy

        while l1 != None and l2 != None:
            current.next, current, l1 = l1, l1, l1.next
            current.next, current, l2 = l2, l2, l2.next

        # return dummy.next
