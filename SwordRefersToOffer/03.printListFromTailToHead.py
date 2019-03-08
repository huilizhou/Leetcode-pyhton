# -*- coding:utf-8 -*-
# 从尾到头打印链表
'''
通常在这种情况下，我们不希望改变原链表的结构。返回一个反序的链表，这就是经典的“后进先出”。
我们可以用栈实现这种结构，每经过一个结点的时候，把该结点放到一个栈中。当遍历完整个链表后。
再从栈顶逐个的输出结点的值，给一个新的链表结构，这样就实现了反转。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        # if not listNode:
        #     return []
        # res = []
        # while listNode:
        #     res.append(listNode.val)
        #     listNode = listNode.next
        # return res[::-1]

        # 人家的写法，类似
        res = []
        while listNode:
            res.insert(0, listNode.val)
            listNode = listNode.next
        return res


L = ListNode(1)
L.next = ListNode(2)
L.next.next = ListNode(3)

print(Solution().printListFromTailToHead(L))
