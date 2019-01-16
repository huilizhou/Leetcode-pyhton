# 合并二叉树
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()

            return repr(serial)

        else:
            return None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 人家的写法
        # if t1 and t2:
        #     node = TreeNode(t1.val + t2.val)
        #     node.left = self.mergeTrees(t1.left, t2.left)
        #     node.right = self.mergeTrees(t1.right, t2.right)
        #     return node
        # else:
        #     return t1 or t2

        # 我的想法
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(2)
t1.left.left = TreeNode(3)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(2)
t2.left.left = TreeNode(4)

print(Solution().mergeTrees(t1, t2))
