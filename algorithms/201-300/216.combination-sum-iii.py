class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def func(start, count, sums, nums):
            if count > k or sums > n:
                return
            if count == k and sums == n:
                result.append(nums)
                return
            for x in range(start + 1, 10):
                func(x, count + 1, sums + x, nums + [x])
        func(0, 0, 0, [])
        return result


print(Solution().combinationSum3(3, 7))
