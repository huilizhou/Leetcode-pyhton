# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        head = root
        while head:
            prev, cur, next_head = None, head, None
            while cur:
                if next_head is None:
                    if cur.left:
                        next_head = cur.left
                    elif cur.right:
                        next_head = cur.right

                if cur.left:
                    if prev:
                        prev.next = cur.left
                    prev = cur.left

                if cur.right:
                    if prev:
                        prev.next = cur.right
                    prev = cur.right

                cur = cur.next
            head = next_head
