# 路径总和II
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # 人家的解法
    #     if root is None:
    #         return []
    #     res = []
    #     self.helper(root, sum, [], res)
    #     return res

    # def helper(self, root, sum, path, res):
    #     if not root.left and not root.right and sum == root.val:
    #         path.append(root.val)
    #         res.append(path)
    #     if root.left:
    #         self.helper(root.left, sum - root.val, path + [root.val], res)
    #     if root.right:
    #         self.helper(root.right, sum - root.val, path + [root.val], res)

        # 人家的解法
        if not root:
            return []
        if root.left == None and root.right == None and root.val == sum:
            return [[root.val]]
        elif root.left == None and root.right == None and root.val != sum:
            return []
        flag = self.pathSum(
            root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        for i in flag:
            i.insert(0, root.val)
        return flag


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
print(Solution().pathSum(root, 22))
