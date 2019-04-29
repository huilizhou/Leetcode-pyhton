# 最小移动次数使数组元素相等
class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 找到中位数，计算所有的数与中位数的差值即可。
        # nums.sort()
        # median = nums[len(nums) // 2]
        # return sum(abs(num - median) for num in nums)

        nums.sort()
        m = len(nums) // 2
        ans = 0
        for i in range(m):
            ans += nums[m] - nums[i]
        for i in range(m, len(nums)):
            ans += nums[i] - nums[m]
        return ans


print(Solution().minMoves2([1, 2, 3]))
