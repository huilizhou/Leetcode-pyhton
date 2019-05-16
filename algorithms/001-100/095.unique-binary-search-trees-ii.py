# 不同的二叉搜索树II
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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genTrees(1, n)

    def genTrees(self, start, end):
        res = []
        if (start > end):
            return [None]
        if start == end:
            node = TreeNode(start)
            res.append(node)
            return res
        for i in range(start, end + 1):
            lnodes = self.genTrees(start, i - 1)
            rnodes = self.genTrees(i + 1, end)
            for lnode in lnodes:
                for rnode in rnodes:
                    node = TreeNode(i)
                    node.left = lnode
                    node.right = rnode
                    res.append(node)
        return res


print(Solution().generateTrees(3))
