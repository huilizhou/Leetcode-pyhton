# -*- coding:utf-8 -*-
# 按之字形顺序打印二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        current, result, level = [pRoot], [], 1
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            if level % 2:
                result.append(vals)
            else:
                result.append(vals[::-1])
            level += 1
        return result
