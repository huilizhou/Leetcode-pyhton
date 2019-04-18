# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # d = dict()
        # while headA:
        #     d[headA] = 1
        #     headA = headA.next
        # while headB:
        #     if headB in d:
        #         return headB
        #     headB = headB.next
        # return None

        # 人家的解法，相当于p1+p2 和p2+p1叠加后同时遍历
        if headA == None or headB == None:
            return None
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 != None else headB
            p2 = p2.next if p2 != None else headA
        return p2


L1 = ListNode(4)
L1.next = ListNode(3)
L1.next.next = ListNode(8)
L1.next.next.next = ListNode(4)
L1.next.next.next.next = ListNode(5)

L2 = ListNode(5)
L2.next = ListNode(0)
L2.next.next = ListNode(1)
L2.next.next.next = ListNode(8)
L2.next.next.next.next = ListNode(4)
L2.next.next.next.next.next = ListNode(5)

print(Solution().getIntersectionNode(L1, L2))
