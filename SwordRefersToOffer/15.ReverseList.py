# -*- coding:utf-8 -*-
# 反转链表


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        dummy = ListNode(0)

        while pHead:
            dummy.next, pHead.next, pHead = pHead, dummy.next, pHead.next
        return dummy.next
