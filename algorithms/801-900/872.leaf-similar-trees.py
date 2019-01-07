# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.root1leaves = []
        self.root2leaves = []
        self.traveltree1(root1)
        self.traveltree2(root2)
        if self.root1leaves == self.root2leaves:
            return True
        else:
            return False

    def traveltree1(self, node):
        if not node:
            return
        if node.left:
            self.traveltree1(node.left)
        if node.right:
            self.traveltree1(node.right)
        if not node.left and not node.right:
            self.root1leaves.append(node.val)
        return

    def traveltree2(self, node):
        if not node:
            return
        if node.left:
            self.traveltree2(node.left)
        if node.right:
            self.traveltree2(node.right)
        if not node.left and not node.right:
            self.root2leaves.append(node.val)
        return
