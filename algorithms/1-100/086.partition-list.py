# 分隔链表
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # dummySmaller, dummyGreater = ListNode(-1), ListNode(-1)
        # smaller, greater = dummySmaller, dummyGreater

        # while head:
        #     if head.val < x:
        #         smaller.next = head
        #         smaller = smaller.next
        #     else:
        #         greater.next = head
        #         greater = greater.next
        #     head = head.next

        # smaller.next = dummyGreater.next
        # greater.next = None

        # return dummySmaller.next

        # 人家的解法同样
        if head == None or head.next == None:
            return head

        cur = head
        pre_min = cur_min = ListNode(-1)
        pre_max = cur_max = ListNode(-1)

        while cur != None:
            if cur.val < x:
                cur_min.next = cur
                cur_min = cur_min.next
            else:
                cur_max.next = cur
                cur_max = cur_max.next

            cur = cur.next

        cur_min.next = pre_max.next
        cur_max.next = None

        return pre_min.next


l = ListNode(1)
l.next = ListNode(4)
l.next.next = ListNode(3)
l.next.next.next = ListNode(2)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(2)


print(Solution().partition(l, 3))
