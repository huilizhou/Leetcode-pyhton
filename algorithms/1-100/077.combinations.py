# 组合
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # from itertools import combinations
        # return list(combinations(range(1, n + 1), k))

        # 人家的解法
        res = []

        def dfs(n, k, start, value):
            if k == len(value):
                res.append(value.copy())
                return
            for i in range(start, n - (k - len(value)) + 2):
                value.append(i)
                dfs(n, k, i + 1, value)
                value.pop()
        if n < k or n < 1 or k < 1:
            return []
        value = []
        dfs(n, k, 1, value)
        return res


print(Solution().combine(4, 2))
