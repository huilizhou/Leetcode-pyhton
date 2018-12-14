# 从中序与后序遍历序列构造二叉树
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 我的想法
        if not len(inorder):
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[0:index], postorder[0:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        return root

        # 人家的解法
    #     lookup = {}
    #     for i, num in enumerate(inorder):
    #         lookup[num] = i
    #     return self.buildTreeRecu(lookup, postorder, inorder, len(postorder), 0, len(inorder))

    # def buildTreeRecu(self, lookup, postorder, inorder, post_end, in_start, in_end):
    #     if in_start == in_end:
    #         return None
    #     node = TreeNode(postorder[post_end - 1])
    #     i = lookup[postorder[post_end - 1]]
    #     node.left = self.buildTreeRecu(
    #         lookup, postorder, inorder, post_end - 1 - (in_end - i - 1), in_start, i)
    #     node.right = self.buildTreeRecu(
    #         lookup, postorder, inorder, post_end - 1, i + 1, in_end)
    #     return node


print(Solution().buildTree(
    inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]))
