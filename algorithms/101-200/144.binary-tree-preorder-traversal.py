# 二叉树的前序遍历
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 我的想法，递归
        res = []
        if not root:
            return res
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
print(Solution().preorderTraversal(tree))
