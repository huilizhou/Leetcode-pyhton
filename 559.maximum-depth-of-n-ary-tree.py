# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        # 我的思路，运行出错
        # if root == None:
        #     return 0
        # return max(self.maxDepth(root.children)) + 1

        if root == None:
            return 0

        depth = 0
        for ch in root.children:
            depth = max(depth, self.maxDepth(ch))

        return depth + 1
