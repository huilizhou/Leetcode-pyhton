# -*- coding:utf-8 -*-
# 合并两个排序链表
'''
先判断输入的链表是否为空，如果第一个链表为空，则直接返回第二个链表；
如果第二个链表为空，则直接返回第一个链表。如果两个链表都为空链表，合并的结果是得到一个空链表

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2
