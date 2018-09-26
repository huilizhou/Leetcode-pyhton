# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归。求中序遍历。
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            ret.append(root.val)
            inorder(root.right)

        ret = []
        inorder(root)

        return ret

        # 人家的解法，递归。
        # res=[]
        # if root != None:
        #     res += self.inorderTraversal(root.left)
        #     res.append(root.val)
        #     res += self.inorderTraversal(root.right)
        # return res


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
print(Solution().inorderTraversal(tree))
