# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

        # 人家的想法
        # if node and node.next:
        #     node_to_delete = node.next
        #     node.val = node_to_delete.val
        #     node.next = node_to_delete.next
        #     del node_to_delete
