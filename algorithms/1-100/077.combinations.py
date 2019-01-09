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

        # 人家的解法，回溯算法
        if k > n:
            return []

        def backtrack(start, stop, num):
            if num == 1:
                return [[i] for i in range(start, stop + 1)]
            ans = []
            for i in range(start, stop - num + 2):
                for suf in backtrack(i + 1, stop, num - 1):
                    ans.append([i] + suf)
            return ans
        return backtrack(1, n, k)


print(Solution().combine(4, 2))
