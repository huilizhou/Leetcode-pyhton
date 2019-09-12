# 环形链表
# Definition for singly-linked list.

'''
双指针
如果列表中不存在换，最终快指针会先到达尾部，此时返回false。
现在考虑一个环形链表，把慢指针和快指针想象成两个在环形赛道上跑步的运动员（分别称之为慢跑者与快跑者）。
而快跑者最终一定会追上慢跑者。这是为什么呢？考虑下面这种情况（记作情况 A）
- 假如快跑者只落后慢跑者一步，在下一次迭代中，它们就会分别跑了一步或两步并相遇。

'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 双指针法
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        # # hash表
        # if not head:
        #     return False

        # target = {head}
        # head = head.next
        # while head:
        #     if head in target:
        #         return True
        #     else:
        #         target.add(head)
        #         head = head.next
        # return False
