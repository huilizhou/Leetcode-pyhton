# 完全二叉树的节点个数
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)
print(Solution().countNodes(tree))
