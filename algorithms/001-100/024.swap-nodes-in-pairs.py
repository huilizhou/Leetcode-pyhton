# 两两交换链表中的结点
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "None"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 我的解法
        if not head or not head.next:
            return head
        node = head
        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        return head

        # 调用了一下递归
        # if not head or not head.next:
        #     return head
        # result = head.next
        # head.next = self.swapPairs(result.next)
        # result.next = head
        # return result


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)


print(Solution().swapPairs(l2))
