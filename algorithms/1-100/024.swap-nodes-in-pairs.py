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
        # 我的想法，分成两个链表即奇数位置链表和偶数位置链表
        # 再将偶数位置和奇数位置链表合并。未完成

        # 人家的解法：
        # 运用temp,结点交换画流程图解决
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            next_one, next_two, next_three = curr.next, curr.next.next, curr.next.next.next
            curr.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            curr = next_one
        return dummy.next

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

print(Solution().swapPairs(l2))
