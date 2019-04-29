# N叉树的层序遍历
# Definition for a Node.


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        cur = [root]
        while cur:
            child = []
            temp = []
            for node in cur:
                temp.append(node.val)
                child += node.children
            res.append(temp)
            cur = child
        return res
