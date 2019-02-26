# -*- coding:utf-8 -*-
# 树的子结构
'''
要查找树A是否存在和树B一样的子树，我们分两步：
第一步在树A中找到和树B的根结点的值一样的结点R，
第二步再判断树A中以R为根节点的子树是不是包含和树B一样的结构。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2) or self.is_subtree(pRoot1, pRoot2)

    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)
