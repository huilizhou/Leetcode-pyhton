# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 人家的解法
        # if root != None:
        #     root.left,root.right= self.invertTree(root.right),self.invertTree(root.left)              
        # return root
            
        if root is None:
            return
        temp=root.left
        root.left=root.right
        root.right=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 


tree = TreeNode(4)
tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right=TreeNode(3)
tree.right=TreeNode(7)
tree.right.left=TreeNode(6)
tree.right.right=TreeNode(9)

print(Solution().invertTree(tree))
    