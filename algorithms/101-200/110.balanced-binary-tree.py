# 平衡二叉树
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 人家的解法
        # def getHeight(root):
        #     if root is None:
        #         return 0
        #     left_height, right_height = \
        #         getHeight(root.left), getHeight(root.right)
        #     if left_height < 0 or right_height < 0 or \
        #        abs(left_height - right_height) > 1:
        #         return -1
        #     return max(left_height, right_height) + 1
        # return (getHeight(root) >= 0)

        # 我的想法
        self.flag = True

        def maxDepth(root):
            if not root:
                return 0
            left_height = maxDepth(root.left)
            right_height = maxDepth(root.right)
            if abs(left_height - right_height) > 1:
                self.flag = False
            return max(left_height, right_height) + 1

        maxDepth(root)
        if self.flag == False:
            return False
        else:
            return True


root = TreeNode(2)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.right = TreeNode(2)
print(Solution().isBalanced(root))
