# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = {}
        self.go(root, res)
        res = sorted(res.items(), key=lambda x: -x[1])
        return [x[0] for x in res if x[1] == res[0][1]]

    def go(self, root, res):
        if root:
            res[root.val] = res.get(root.val, 0) + 1
            self.go(root.left, res)
            self.go(root.right, res)
