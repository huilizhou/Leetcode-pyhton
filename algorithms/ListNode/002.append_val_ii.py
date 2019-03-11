'''
在给定节点前添加结点

1.使用给定值初始化新结点cur
2.将cur的next字段链接到prev的下一个结点next
3.将prev中的next字段链接到cur

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
    def add_val(self, head):
        dummy = ListNode(0)
        dummy.next = head.next
        head.next = dummy
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print(Solution().add_val(head))
