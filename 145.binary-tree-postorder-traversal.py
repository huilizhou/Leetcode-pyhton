# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postorder(root):
            if not root:
                return

            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = []
        postorder(root)

        return res

        # 人家的解法，递归，同上
        # ans=[]
        # if(root==None):
        #     return []
        # ans+=self.postorderTraversal(root.left)
        # ans+=self.postorderTraversal(root.right)
        # ans.append(root.val)
        # return ans


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

print(Solution().postorderTraversal(tree))
