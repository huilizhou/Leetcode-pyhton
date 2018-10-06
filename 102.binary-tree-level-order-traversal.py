# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 人家的解法，一层层遍历，我目前还未想到更好的解法
        if not root:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                current = next_level
                result.append(vals)
        return result

        #   人家用队列的解法
        # res = []
        # # 如果根节点为空，则返回空列表
        # if root is None:
        #     return res
        # # 模拟一个队列储存节点
        # q = []
        # # 首先将根节点入队
        # q.append(root)
        # # 列表为空时，循环终止
        # while len(q) != 0:
        #     # 使用列表存储同层节点
        #     tmp = []
        #     # 记录同层节点的个数
        #     length = len(q)
        #     for i in range(length):
        #         # 将同层节点依次出队
        #         r = q.pop(0)
        #         if r.left is not None:
        #             # 非空左孩子入队
        #             q.append(r.left)
        #         if r.right is not None:
        #             # 非空右孩子入队
        #             q.append(r.right)
        #         tmp.append(r.val)
        #     res.append(tmp)
        # return res
