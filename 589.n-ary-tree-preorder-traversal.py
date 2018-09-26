
# Definition for a Node.


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 人家的解法，树的问题采用递归的解法
        def dfs(root, result):
            result.append(root.val)
            for child in root.children:
                if child:
                    dfs(child, result)

        result = []
        if root:
            dfs(root, result)
        return result
