# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


l = TreeNode(1)
l.left = TreeNode(9)
l.right = TreeNode(20)
l.left.left = TreeNode(None)
l.left.right = TreeNode(None)
l.right.left = TreeNode(15)
l.right.right = TreeNode(7)

print(Solution().maxDepth(l))
