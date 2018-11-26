# 反转链表
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # dummy = ListNode(float('-inf'))

        # while head:
        #     dummy.next, head.next, head = head, dummy.next, head.next

        # return dummy.next

        # 一种解法
        # pre = None
        # cur = head

        # while cur != None:
        #     lat = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = lat
        # return pre

        # 第二种解法 使用递归的方法
        if head == None or head.next == None:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)


print(Solution().reverseList(l))
