# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 我的想法
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res = res[::2] + res[1::2]
        return res

        # 人家的解法
        # if head == None or head.next == None:
        #     return head

        # odd = head
        # even = head.next
        # t = even
        # while even != None and even.next != None:
        #     odd.next = even.next
        #     odd = odd.next
        #     even.next = odd.next
        #     even = even.next
        # odd.next = t
        # return head


l = ListNode(1)
l.next = ListNode(4)
l.next.next = ListNode(3)
l.next.next.next = ListNode(2)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(2)

print(Solution().oddEvenList(l))
