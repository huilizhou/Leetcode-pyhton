class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k - 1]


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], k=2))
