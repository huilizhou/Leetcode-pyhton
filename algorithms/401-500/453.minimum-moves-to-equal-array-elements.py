# 最小移动次数使数组元素相等
class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 逆向思考， n-1个数同时加一，就好比每次有一个数自身减一，因为只能做减法，
        # 所以数组最后的数只能是最小值。这样的话每个元素减去最小值求其和就是答案
        # return sum(nums) - min(nums) * len(nums)

        # 人家的写法
        sum = 0
        min_val = min(nums)
        for num in nums:
            sum += num - min_val
        return sum


print(Solution().minMoves([1, 2, 3]))
