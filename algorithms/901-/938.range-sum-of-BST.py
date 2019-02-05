# 二叉搜索树的范围和
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        else:
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)


tree = TreeNode(10)
tree.left = TreeNode(5)
tree.right = TreeNode(15)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(7)
tree.right.right = TreeNode(18)


print(Solution().rangeSumBST(tree, L=7, R=15))
