# 二叉搜索树的最近公共祖先
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if q.val >= root.val >= p.val or q.val <= root.val <= p.val:
        #     return root
        # elif q.val > root.val and p.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # elif q.val < root.val and p.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return None

        # 人家的写法
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


tree = TreeNode(6)
tree.left = TreeNode(2)
tree.right = TreeNode(8)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(4)
tree.left.right.left = TreeNode(3)
tree.left.right.right = TreeNode(5)
tree.right.left = TreeNode(7)
tree.right.right = TreeNode(9)

print(Solution().lowestCommonAncestor(tree, p=TreeNode(2), q=TreeNode(8)))
