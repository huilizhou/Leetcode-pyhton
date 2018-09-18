# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # # 这个是小强哥github上的，我没有看懂。
        dummy = ListNode(float('-inf'))

        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

        # 建立一个空链表，在空链表中反转
        # lst = []
        # p = head
        # while p:
        #     lst.append(p.val)
        #     p = p.next

        # return lst[::-1]

        # if head == None:
        #     return None
        # p = head
        # q = head.next
        # head.next = None
        # while q != None:
        #     p = q
        #     q = p.next
        #     p.next = head
        #     head = p
        # return head


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)


print(Solution().reverseList(l))
