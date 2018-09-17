class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[k - 1]


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], k=2))
