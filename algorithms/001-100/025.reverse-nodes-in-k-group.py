# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # # 先遍历一遍链表，统计链表长度，然后每k个链表做反转操作
        # # 遍历链表的过程中，每k个链表做反转操作
        h = ListNode(-1)
        h.next = head
        pre = h
        cur = head

        while cur != None:
            t = cur
            count = 1
            while count < k and t != None:
                t = t.next
                count += 1
            if count == k and t != None:
                for _ in range(k - 1):
                    lat = cur.next
                    cur.next = lat.next
                    lat.next = pre.next
                    pre.next = lat
                pre = cur
                cur = pre.next
            else:
                break

        return h.next

        # 人家的解法
    #     dummy = ListNode(-1)
    #     dummy.next = head

    #     cur, cur_dummy = head, dummy
    #     length = 0

    #     while cur:
    #         next_cur = cur.next
    #         length = (length + 1) % k

    #         if length == 0:
    #             next_dummy = cur_dummy.next
    #             self.reverse(cur_dummy, cur.next)
    #             cur_dummy = next_dummy

    #         cur = next_cur
    #     return dummy.next

    # def reverse(self, begin, end):
    #     first = begin.next
    #     cur = first.next

    #     while cur != end:
    #         first.next = cur.next
    #         cur.next = begin.next
    #         begin.next = cur
    #         cur = first.next


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)

print(Solution().reverseKGroup(l2, 2))
