# -*- coding:utf-8 -*-
# 链表中环的入口结点
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow, fast = pHead, pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = pHead
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        return None
