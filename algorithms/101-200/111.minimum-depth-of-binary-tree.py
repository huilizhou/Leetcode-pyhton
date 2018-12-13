# 二叉树的最小深度
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 我的想法
        # 由题意，最小深度是从根节点到最近的叶子节点的最短路径的节点的数量。
        # 一开始，理解不对，必须是从根节点到叶子节点
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return 1 + self.minDepth(root.right)
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min([self.minDepth(root.left), self.minDepth(root.right)])


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
print(Solution().minDepth(tree))
