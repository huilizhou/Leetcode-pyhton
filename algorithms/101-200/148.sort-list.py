# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 我的想法
        if not head:
            return
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.sort()
        return res


L = ListNode(4)
L.next = ListNode(3)
L.next.next = ListNode(1)
L.next.next.next = ListNode(2)
print(Solution().sortList(L))
