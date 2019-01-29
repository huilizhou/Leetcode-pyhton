# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []

        def returnval(root):
            if root.left == None and root.right == None:
                return [str(root.val)]
            else:
                result = []
                if root.left != None:
                    for i in returnval(root.left):
                        result.append(str(root.val) + '->' + str(i))
                if root.right != None:
                    for i in returnval(root.right):
                        result.append(str(root.val) + '->' + str(i))
                return result
        return returnval(root)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(5)
print(Solution().binaryTreePaths(tree))
