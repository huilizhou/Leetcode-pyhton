# 对称二叉树
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
        # 人家的写法(2种，递归法和迭代法)
        return self.ismirror(root, root)
    # 递归法

    # def ismirror(self, p, q):
    #     if not p and not q:
    #         return True
    #     elif not p or not q:
    #         return False
    #     elif p.val == q.val:
    #         return self.ismirror(p.left, q.right) and self.ismirror(p.right, q.left)
    #     else:
    #         return False

    # 迭代法，没懂
    def ismirror(self, l_root, r_root):
        qlist = []
        qlist.append(l_root)
        qlist.append(r_root)
        while len(qlist) != 0:
            t1 = qlist.pop()
            t2 = qlist.pop()
            if(t1 == None and t2 == None):
                continue
            if(t1 == None or t2 == None):
                return False
            if(t1.val != t2.val):
                return False
            qlist.append(t1.left)
            qlist.append(t2.right)
            qlist.append(t1.right)
            qlist.append(t2.left)
        return True


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)

print(Solution().isSymmetric(tree))
