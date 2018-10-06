# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 人家的解法判断左子树。及其值
        # def sumOfLeftLeavesHelper(root, is_left):
        #     if not root:
        #         return 0
        #     if not root.left and not root.right:
        #         return root.val if is_left else 0
        #     return sumOfLeftLeavesHelper(root.left, True) + \
        #         sumOfLeftLeavesHelper(root.right, False)

        # return sumOfLeftLeavesHelper(root, False)

        #  人家的解法：
        # if not root:
        #     return 0
        # if root.left and not root.left.left and not root.left.right:
        #     return root.left.val + self.sumOfLeftLeaves(root.right)
        # return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        if root == None:
            return 0

        sum = 0
        nodes = list()
        nodes.append(root)

        while nodes:
            node = nodes.pop()
            if node.left:
                if node.left.left == None and node.left.right == None:
                    sum += node.left.val
                else:
                    nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return sum


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(Solution().sumOfLeftLeaves(tree))
