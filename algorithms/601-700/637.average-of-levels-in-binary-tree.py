# 二叉树的层平均值
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
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # result = []
        # q = [root]
        # while q:
        #     total, count = 0, 0
        #     next_q = []
        #     for n in q:
        #         total += n.val
        #         count += 1
        #         if n.left:
        #             next_q.append(n.left)
        #         if n.right:
        #             next_q.append(n.right)
        #     q = next_q
        #     result.append(float(total) / count)
        # return result

        # 人家的解法
        result = []

        def dfs(node, depth=0):
            if node:
                if len(result) <= depth:
                    result.append([0, 0])
                result[depth][0] += node.val
                result[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)
        return [s / float(v) for s, v in result]


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
print(Solution().averageOfLevels(tree))
