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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 我的想法
        if not nums:
            return None
        mid = len(nums) // 2  # 找到中间节点
        root = TreeNode(nums[mid])  # 当前节点为根节点
        root.left = self.sortedArrayToBST(nums[:mid])  # 小于当前根节点的作为左子树
        root.right = self.sortedArrayToBST(nums[mid + 1:])  # 大于当前根节点的作为右子树
        return root


print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
