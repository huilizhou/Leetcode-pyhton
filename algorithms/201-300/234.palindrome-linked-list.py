# 回文链表
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #  我的想法
        l = []
        if head == None:
            return True
        while head:
            l.append(head.val)
            head = head.next
        return l == l[::-1]

        #  人家的解法。我以为还是我的想法简单一点啊
        #  翻转前部分链表和后半部分链表进行对比。但是他的空间复杂度为O(1)
        # rev = None
        # slow = fast = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     rev, rev.next, slow = slow, rev, slow.next
        # if fast:
        #     slow = slow.next
        # while rev and rev.val == slow.val:
        #     slow = slow.next
        #     rev = rev.next
        # return not rev


l = ListNode(0)
l.next = ListNode(0)


print(Solution().isPalindrome(l))
