# 删除排序链表中的重复元素II
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 人家的做法
        dummy = ListNode(0)
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.next.val == cur.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        return dummy.next

        # 我的想法。空间复杂度高了点儿
        # tmp = []
        # result = []
        # r = []
        # while head:
        #     result.append(head.val)
        #     if head.next:
        #         if head.val == head.next.val:
        #             tmp.append(head.val)
        #     head = head.next

        # for i in result:
        #     if i not in tmp:
        #         r.append(i)
        # return r


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(2)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)
l.next.next.next.next.next = ListNode(5)
l.next.next.next.next.next.next = ListNode(6)

print(Solution().deleteDuplicates(l))
