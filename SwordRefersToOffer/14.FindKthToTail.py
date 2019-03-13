# -*- coding:utf-8 -*-
# 链表中倒数第k个结点
'''
我们可以定义两个指针。第一个指针从链表的头指针开始遍历向前走k-1，第二个指针保持不动；
从第k步开始，第二个指针也开始从链表的头指针开始遍历。由于两个指针的距离保持在k-1，当第一个指针到达链表的尾节点时
第二个指针正好是倒数第k个节点。

'''


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
    def FindKthToTail(self, head, k):
        # write code here
        # l = []
        # while head:
        #     l.append(head)
        #     head = head.next
        # if len(l) < k or k < 1:
        #     return None
        # return l[-k]

        if head == None or k == 0:
            return None
        phead = head
        pbehind = head
        for _ in range(k - 1):
            if phead.next == None:
                return None
            else:
                phead = phead.next
        while phead.next != None:
            phead = phead.next
            pbehind = pbehind.next
        return pbehind


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print(Solution().FindKthToTail(head, 1))
