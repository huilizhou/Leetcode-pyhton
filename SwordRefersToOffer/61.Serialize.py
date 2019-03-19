# -*- coding:utf-8 -*-
# 序列化二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        serialzieStr = ""
        if root == None:
            return "#"
        stack = []
        while root or stack:
            while root:
                serialzieStr += str(root.val) + ","
                stack.append(root)
                root = root.left
            serialzieStr += "#,"
            root = stack.pop()
            root = root.right
        serialzieStr = serialzieStr[:-1]
        return serialzieStr

    def Deserialize(self, s):
        serialize = s.split(',')
        tree, sp = self.deserialize(serialize, 0)
        return tree

    def deserialize(self, s, sp):
        if sp >= len(s) or s[sp] == '#':
            return None, sp + 1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.deserialize(s, sp)
        node.right, sp = self.deserialize(s, sp)
        return node, sp
