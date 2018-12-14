# 从前序与中序遍历序列构造二叉树
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 我的想法
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root

        # 人家的解法
    #     lookup = {}
    #     for i, num in enumerate(inorder):
    #         lookup[num] = i
    #     return self.buildTreeRecu(lookup, preorder, inorder, 0, 0, len(inorder))

    # def buildTreeRecu(self, lookup, preorder, inorder, pre_start, in_start, in_end):
    #     if in_start == in_end:
    #         return None
    #     node = TreeNode(preorder[pre_start])
    #     i = lookup[preorder[pre_start]]
    #     node.left = self.buildTreeRecu(
    #         lookup, preorder, inorder, pre_start + 1, in_start, i)
    #     node.right = self.buildTreeRecu(
    #         lookup, preorder, inorder, pre_start + 1 + i - in_start, i + 1, in_end)
    #     return node


print(Solution().buildTree(
    preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
