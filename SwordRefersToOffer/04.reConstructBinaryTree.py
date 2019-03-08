# -*- coding:utf-8 -*-
# 重建二叉树
'''
在二叉树前序遍历序列中，第一个数字总是树的根结点的值。
但在中序遍历序列中，根结点的值在序列的中间，左子树结点的值位于根结点值的左边，右子树的根结点的值位于根结点的右边。
因此我们需要扫描中序遍历序列，找到根节点的值。
前序遍历序列的第一个数字1就是根结点的值。扫描中序遍历序列，就能确定根结点值的位置。
分别找到左右子树的前序和中序遍历序列，我们就可以通过同样的方式构建左右子树。这就是一个递归的过程。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            pos = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:pos + 1], tin[:pos])
            root.right = self.reConstructBinaryTree(
                pre[pos + 1:], tin[pos + 1:])
        return root
