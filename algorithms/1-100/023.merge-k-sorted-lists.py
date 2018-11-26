# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # # 我的解法
        n = len(lists)
        l = []
        for i in range(n):
            while(lists[i] != None):
                l.append(lists[i].val)
                lists[i] = lists[i].next
        result = sorted(l)
        return result

        # 人家的解法
        # if not lists:
        #     return None
        # res = []
        # for i in lists:
        #     head = i
        #     while head:
        #         res.append(head.val)
        #         head = head.next
        # res.sort()
        # head = ListNode(0)
        # r = head
        # for i in res:
        #     r.next = ListNode(i)
        #     r = r.next
        # return head.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(5)
l3.next.next = ListNode(7)

lists = [l1, l2, l3]
print(Solution().mergeKLists(lists))
