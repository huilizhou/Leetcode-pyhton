# 环形链表II
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 我的理解
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None


"""
\\141,142题做一个小结。
设表头是X，环的第一个节点是Y，slow和fast第一次的交点是Z。各段的长度是a,b,c。
第一次相遇是slow走过的长度是a+b，fast走过的长度是a+b+c+b。
所以有a=c，此时，另fast为head,fast和slow同时一步一步走相交的那个点即为环的入口。
"""
