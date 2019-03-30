# -*- coding:utf-8 -*-
# 二叉搜索树的第k个结点


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.treeNode = []

    def inOrder(self, pRoot):
        if len(self.treeNode) < 0:
            return None
        if pRoot.left:
            self.inOrder(pRoot.left)
        self.treeNode.append(pRoot)
        if pRoot.right:
            self.inOrder(pRoot.right)

    def KthNode(self, pRoot, k):
        if k == 0 or pRoot == None:
            return
        self.inOrder(pRoot)
        if len(self.treeNode) < k:
            return None
        return self.treeNode[k - 1]
