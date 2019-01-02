class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # 思路，实际上就是ops的最小范围中的个数
        # 人家的写法
        # return min(i[0] for i in ops) * min(i[1] for i in ops) if ops else m * n

        # 我的写法
        for op in ops:
            if op[0] < m:
                m = op[0]
            if op[1] < n:
                n = op[1]
        return m * n


print(Solution().maxCount(3, 3, [[2, 2], [3, 3], [3, 1]]))
