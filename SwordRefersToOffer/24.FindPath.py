# -*- coding:utf-8 -*-
# 二叉树中和为某一值的路径
'''
深度优先搜索。使用前序遍历。每次遍历前，我们先把root值压入tmp，然后判断当前root是否同时满足
1.与给定数值相减为0；2.左子树为空；3.右子树为空；
如果同时满足条件，就将tmp压入到result中，否则，依次遍历左右子树。

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root.left == None and root.right == None and root.val == expectNumber:
            return [[root.val]]
        elif root.left == None and root.right == None and root.val != expectNumber:
            return []
        flag = self.FindPath(root.left, expectNumber - root.val) + \
            self.FindPath(root.right, expectNumber - root.val)
        for i in flag:
            i.insert(0, root.val)
        return flag


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
print(Solution().FindPath(root, 22))
