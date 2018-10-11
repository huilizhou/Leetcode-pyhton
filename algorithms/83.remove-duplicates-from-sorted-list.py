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
        dummy = ListNode(0)
        dummy.next = head

        ret, current = dummy, dummy.next
        if dummy.next == None:
            return None
        else:
            while current.next and head.next != None:
                if current.next.val == current.val:
                    ret.next = current.next
                else:
                    ret = current
                current = current.next
            return dummy.next

        # # 人家的解法
        # dummy = ListNode(None)
        # dummy.next = head
        # p = dummy
        # while p and p.next:
        #     if p.val == p.next.val:
        #         p.next = p.next.next
        #     else:
        #         p = p.next

        #     return dummy.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(2)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)
l.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next = ListNode(6)

print(Solution().deleteDuplicates(l))
