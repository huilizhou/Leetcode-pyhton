# 二叉树的层次遍历II
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result[::-1]

        # 人家的解法
        # res = []

        # def addToList(node, dep):
        #     if not node:
        #         return
        #     if dep >= len(res):
        #         res.append([])
        #     res[dep].append(node.val)
        #     if node.left:
        #         addToList(node.left, dep + 1)
        #     if node.right:
        #         addToList(node.right, dep + 1)

        # addToList(root, 0)
        # return res[::-1]


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(Solution().levelOrderBottom(tree))
