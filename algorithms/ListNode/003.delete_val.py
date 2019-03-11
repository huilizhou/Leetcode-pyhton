'''
如果我们想从单链表中删除现有的结点cur，可以分两步完成
1.找到cur的上一个结点prev以及期下一个结点next.
2.接下来链接prev到cur的下一个结点next。

在第一步中，我们需要找到prev和next
但是我们必须从头结点遍历链表，以找出prev，它的平均时间是O(N)，其中N是链表的长度。
因此删除结点的时间复杂度将是O(N)。空间复杂度为O(1)，因为我们只需要常量空间来存储指针。
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "None"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def deleteNode(self, head, node):
        node.val = node.next.val
        node.next = node.next.next
