# -*- coding:utf-8 -*-
# 从上往下打印二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        result = []
        tmp = [root]
        while len(tmp):
            cur = tmp.pop(0)
            result.append(cur.val)
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
        return result


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
print(Solution().PrintFromTopToBottom(tree))
