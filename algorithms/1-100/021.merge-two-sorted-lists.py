# 合并两个有序链表
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "None"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 我的想法
        # l = []
        # while(l1 != None or l2 != None):
        #     if (l1 != None):
        #         l.append(l1.val)
        #         l1 = l1.next
        #     if (l2 != None):
        #         l.append(l2.val)
        #         l2 = l2.next
        # result = sorted(l)
        # return result

        # 人家解法
        # curr = dummy = ListNode(0)

        # while l1 and l2:
        #     if l1.val < l2.val:
        #         curr.next = l1
        #         l1 = l1.next
        #     else:
        #         curr.next = l2
        #         l2 = l2.next
        #     curr = curr.next
        # curr.next = l1 or l2

        # return dummy.next

        # 人家的解法，采用递归的思想
        # if l1 == None:
        #     return l2
        # if l2 == None:
        #     return l1
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

print(Solution().mergeTwoLists(l1, l2))
