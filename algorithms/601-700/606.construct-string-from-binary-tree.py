# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        #  人家的解法，20181005，关于树运用递归的解法，很不熟练感觉。
        # if not t:
        #     return ""
        # s = str(t.val)
        # if t.left or t.right:
        #     s += "(" + self.tree2str(t.left) + ")"
        # if t.right:
        #     s += "(" + self.tree2str(t.right) + ")"
        # return s

        # 人家的解法
        if not t:
            return ""
        res = ""
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if left or right:
            res += "(%s)" % left
        if right:
            res += "(%s)" % right
        return str(t.val) + res


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.right = TreeNode(4)

print(Solution().tree2str(tree))
