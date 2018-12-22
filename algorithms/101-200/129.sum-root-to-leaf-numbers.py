# 求根到叶子结点数字之和
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #     return 0
        # if root.left == None and root.right == None:
        #     self.res += root.val
        # if root.left:
        #     root.left.val += 10 * root.val
        # if root.right:
        #     root.right.val += 10 * root.val

        # self.sumNumbers(root.left)
        # self.sumNumbers(root.right)
        # return self.res

        # 人家的解法
        if not root:
            return 0
        self.s = 0
        self.dfs(root, 0)
        return self.s

    def dfs(self, root, tmp):
        if not root.left and not root.right:
            self.s += 10 * tmp + root.val

        if root.left:
            self.dfs(root.left, tmp * 10 + root.val)
        if root.right:
            self.dfs(root.right, tmp * 10 + root.val)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().sumNumbers(root))
