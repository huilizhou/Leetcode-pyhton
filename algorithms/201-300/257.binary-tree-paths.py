# 二叉树的所有路径
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
        # 人家的解法
        # if root == None:
        #     return []

        # def returnval(root):
        #     if root.left == None and root.right == None:
        #         return [str(root.val)]
        #     else:
        #         result = []
        #         if root.left != None:
        #             for i in returnval(root.left):
        #                 result.append(str(root.val) + '->' + str(i))
        #         if root.right != None:
        #             for i in returnval(root.right):
        #                 result.append(str(root.val) + '->' + str(i))
        #         return result
        # return returnval(root)

        # 人家的写法
        # if not root:
        #     return []
        # if not root.left and not root.right:
        #     return [str(root.val)]
        # paths = self.binaryTreePaths(
        #     root.left) + self.binaryTreePaths(root.right)
        # for i in range(len(paths)):
        #     paths[i] = str(root.val) + "->" + paths[i]
        # return paths

        # 我的想法
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        pathList = []
        if root.left:
            pathList += self.binaryTreePaths(root.left)
        if root.right:
            pathList += self.binaryTreePaths(root.right)
        for index, path in enumerate(pathList):
            pathList[index] = str(root.val) + "->" + path
        return pathList


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

print(Solution().binaryTreePaths(tree))
