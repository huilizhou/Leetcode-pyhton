# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 人家的解法
        # index = [0]

        # def getRes(node, num):
        #     if not node:
        #         return 0
        #     res = getRes(node.left, num)
        #     if index[0] == num:
        #         return res
        #     index[0] += 1
        #     if index[0] == num:
        #         return node.val
        #     return getRes(node.right, num)
        # return getRes(root, k)

        # 我的想法
        def Search(root):
            res = []
            if not root:
                return []
            res.extend(Search(root.left))
            res.append(root.val)
            res.extend(Search(root.right))
            return res

        vals = Search(root)
        return vals[k - 1]


tree = TreeNode(3)
tree.left = TreeNode(1)
tree.right = TreeNode(4)
tree.left.right = TreeNode(2)
print(Solution().kthSmallest(tree, 1))
