# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 人家的解法
        if not root:
            return []
        ret = [root.val]

        from collections import deque
        q = deque()
        q.append((root, 0))
        lv = 0
        while q:
            nd, cur = q.popleft()
            if cur == lv + 1:
                ret.append(nd.val)
                lv += 1
            if nd.right:
                q.append((nd.right, lv + 1))
            if nd.left:
                q.append((nd.left, lv + 1))
        return ret


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(4)

print(Solution().rightSideView(tree))
