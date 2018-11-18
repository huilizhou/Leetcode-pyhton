# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 采用递归的解法，参考小强哥github.思路有，20180928没写出来。
        if not nums:
            return None

        num_max = max(nums)
        max_index = nums.index(num_max)

        left, right = nums[:max_index], nums[max_index + 1:]

        tree = TreeNode(num_max)
        tree.left = self.constructMaximumBinaryTree(left)
        tree.right = self.constructMaximumBinaryTree(right)

        return tree


print(Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))
