class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 我的想法。
        '''
        dp[i][j]表示以第i行第j列为右下角所能构成的最大正方形边长，则递推式为：
        dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]);

        '''

        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_len = 0
        for i in range(0, m):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                max_len = 1
        for j in range(0, n):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                max_len = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1]
                                   [j], dp[i][j - 1]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len * max_len

        # 人家的想法，20190101没看明白
        # if (not matrix) or (not matrix[0]):
        #     return 0
        # n = len(matrix[0])
        # heights = [0] * n
        # k = 0
        # for row in matrix:
        #     for i in range(n):
        #         heights[i] = heights[i] + 1 if row[i] == '1' else 0

        #     freq = 0  # 记录连续有几组值大于等于高度size
        #     for c in heights:
        #         if c > k:
        #             freq += 1
        #             if freq > k:
        #                 k += 1
        #                 break
        #         else:
        #             freq = 0

        # return k * k


print(Solution().maximalSquare(
    [['1', '0', '1', '0', '1'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]))
