# -*- coding:utf-8 -*-
# 两个链表的第一个公共结点
'''
我们可以把两个链表拼接起来，一个pHead1在前pHead2在后，一个pHead2在前pHead1在后。
这样生成了两个相同长度的链表，那么我们只要同时遍历这两个链表，就一定能找到公共结点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here

        # d = dict()
        # while pHead1:
        #     d[pHead1] = 1
        #     pHead1 = pHead1.next
        # while pHead2:
        #     if pHead2 in d:
        #         return pHead2
        #     pHead2 = pHead2.next
        # return None

        if pHead1 == None or pHead2 == None:
            return None
        cur1, cur2 = pHead1, pHead2
        while cur1 != cur2:
            cur1 = cur1.next if cur1 != None else pHead2
            cur2 = cur2.next if cur2 != None else pHead1
        return cur1
