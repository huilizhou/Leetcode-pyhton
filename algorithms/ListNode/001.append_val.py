'''
在开头添加结点

我们用头结点来代表整个列表
1.初始化一个新结点cur
2.将新结点链接到我们的原始头结点head
3.将cur指定为head
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
    def add_val_beforehead(self, head):
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print(Solution().add_val_beforehead(head))
