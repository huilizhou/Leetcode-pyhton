# 找树左下角的值
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS
        # lst, res = [root], float("inf")
        # while lst:
        #     c = len(lst)
        #     res = lst[0].val
        #     while c > 0:
        #         node = lst.pop(0)
        #         if node.left:
        #             lst.append(node.left)
        #         if node.right:
        #             lst.append(node.right)
        #         c -= 1
        # return res

        # 人家的解法
        if not root:
            return None
        queue = [root]
        while(queue):
            left = queue[0].val
            for _ in range(len(queue)):
                tmpNode = queue[0]
                if tmpNode.left:
                    queue.append(tmpNode.left)
                if tmpNode.right:
                    queue.append(tmpNode.right)
                del queue[0]
        return left


tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)

print(Solution().findBottomLeftValue(tree))
