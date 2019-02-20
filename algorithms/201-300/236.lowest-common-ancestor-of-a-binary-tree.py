# 二叉树的最近公共祖先
# Definition for a binary tree node.
'''
我的想法
由说明知，p,q为不同节点且均存在于给定的二叉树中
递归思想，以root为根的(子)树进行查找p和q。如果root=None or p or q，直接返回root。
表示当前的树已经查找完毕，否则对左右子树进行查找，根据左右子树的返回值判断。
如果左子树为空，说明两个节点一定在右子树。同理，如果右子树为空，说明两个节点一定在左子树。
'''


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
        if not root:
            return root

        if (root == p or root == q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


tree = TreeNode(6)
tree.left = TreeNode(2)
tree.right = TreeNode(8)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(4)
tree.left.right.left = TreeNode(3)
tree.left.right.right = TreeNode(5)

print(Solution().lowestCommonAncestor(tree, p=TreeNode(2), q=TreeNode(8)))
