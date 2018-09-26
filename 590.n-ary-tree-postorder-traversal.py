# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 人家的解法，树的问题采用递归的解法
        def dfs(root, result):
            for child in root.children:
                if child:
                    dfs(child, result)
            result.append(root.val)

        result = []
        if root:
            dfs(root, result)
        return result
