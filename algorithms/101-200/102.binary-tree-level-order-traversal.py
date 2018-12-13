# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 人家的解法，一层层遍历，我目前还未想到更好的解法
        if not root:
            return []
        curList = [root]
        rList = []
        while curList:
            tempNodeList = []
            tempValList = []
            for node in curList:
                tempValList.append(node.val)
                if node.left is not None:
                    tempNodeList.append(node.left)
                if node.right is not None:
                    tempNodeList.append(node.right)
                curList = tempNodeList
                rList.append(tempNodeList)
        return rList


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(Solution().levelOrder(tree))
