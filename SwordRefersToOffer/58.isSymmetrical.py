# -*- coding:utf-8 -*-
# 对称二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return self.isSymmetricalCor(pRoot, pRoot)

    def isSymmetricalCor(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSymmetricalCor(pRoot1.left, pRoot2.right) and self.isSymmetricalCor(pRoot1.right, pRoot2.left)
