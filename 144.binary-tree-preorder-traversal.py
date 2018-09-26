# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归的算法求解二叉树的先序遍历
        def preorder(root):
            if not root:
                return

            ret.append(root.val)
            preorder(root.left)
            preorder(root.right)

        ret = []
        preorder(root)

        return ret

        # 人家的解法
        # ans = []
        # if not root:
        #     return []
        # ans.append(root.val)
        # ans += self.preorderTraversal(root.left)
        # ans += self.preorderTraversal(root.right)

        return ans


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
print(Solution().preorderTraversal(tree))
