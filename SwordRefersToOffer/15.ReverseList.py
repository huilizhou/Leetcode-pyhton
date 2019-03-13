# -*- coding:utf-8 -*-
# 反转链表


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
    # 返回ListNode
    # def ReverseList(self, pHead):
        # write code here
        # dummy = ListNode(0)

        # while pHead:
        #     dummy.next, pHead.next, pHead = pHead, dummy.next, pHead.next
        # return dummy.next

    def ReverseList(self, head):
        if not head or not head.next:
            return head
        last = None
        while head:
            temp = head.next
            head.next = last
            last = head
            head = temp
        return last


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print(Solution().ReverseList(head))
