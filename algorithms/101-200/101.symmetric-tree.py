# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 我的想法，递归
        def ist(left, right):
            if left == None and right == None:
                return True
            if (left == None and right != None) or(left != None and right == None):
                return False

            return left.val == right.val and ist(left.left, right.right) and ist(left.right, right.left)

        if(root == None):
            return True
        return ist(root.left, root.right)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)

print(Solution().isSymmetric(tree))
