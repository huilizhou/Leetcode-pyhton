# 单值二叉树
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 我的想法，分情况讨论
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left:
            return root.val == root.right.val and self.isUnivalTree(root.right)
        if not root.right:
            return root.val == root.left.val and self.isUnivalTree(root.left)
        return root.val == root.left.val and root.val == root.right.val and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

        # 人家的写法
        # if not root:
        #     return False
        # val = root.val
        # stack = []
        # stack.append(root)
        # while stack:
        #     q = stack.pop()
        #     if val != q.val:
        #         return False
        #     else:
        #         if q.left:
        #             stack.append(q.left)
        #         if q.right:
        #             stack.append(q.right)
        # return True


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)


print(Solution().isUnivalTree(tree))
