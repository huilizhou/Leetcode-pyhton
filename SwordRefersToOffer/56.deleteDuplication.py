# -*- coding:utf-8 -*-
# 删除链表中重复的结点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        dummy = ListNode(0)
        pre, cur = dummy, pHead
        while cur:
            if cur.next and cur.next.val == cur.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
            else:
                pre.next=cur
                pre=cur
                cur=cur.next
        return dummy.next
