# 二叉树中的最大路径和
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 人家的解法

        self.res = -float("inf")
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        self.res = max(self.res, left + right + root.val)
        return root.val + max(left, right)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(Solution().maxPathSum(root))
