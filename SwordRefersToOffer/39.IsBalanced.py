# -*- coding:utf-8 -*-
# 平衡二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, root):
        # write code here
        def getHeight(root):
            if root is None:
                return 0
            left_height, right_height = getHeight(
                root.left), getHeight(root.right)
            if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return (getHeight(root) >= 0)
