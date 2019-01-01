class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        # 我的想法，分情况讨论
        m = len(M)
        n = len(M[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if m == 1:
            if n == 1:
                dp[0][0] = M[0][0]
                return dp
            else:
                dp[0][0] = (M[0][0] + M[0][1]) // 2
                dp[0][n - 1] = (M[0][n - 1] + M[0][n - 2]) // 2
                for j in range(1, n - 1):
                    dp[0][j] = (M[0][j - 1] + M[0][j] + M[0][j + 1]) // 3
                return dp

        if n == 1:
            if m == 1:
                dp[0][0] = M[0][0]
                return dp
            else:
                dp[0][0] = (M[0][0] + M[1][0]) // 2
                dp[m - 1][0] = (M[m - 1][0] + M[m - 2][0]) // 2
                for i in range(1, m - 1):
                    dp[i][0] = (M[i - 1][0] + M[i][0] + M[i + 1][0]) // 3
                return dp

        dp[0][0] = (M[0][0] + M[0][1] + M[1][0] + M[1][1]) // 4
        dp[m - 1][0] = (M[m - 2][0] + M[m - 1][0] +
                        M[m - 2][1] + M[m - 1][1]) // 4
        dp[0][n - 1] = (M[0][n - 2] + M[0][n - 1] +
                        M[1][n - 2] + M[1][n - 1]) // 4
        dp[m - 1][n - 1] = (M[m - 2][n - 2] + M[m - 2]
                            [n - 1] + M[m - 1][n - 2] + M[m - 1][n - 1]) // 4

        for i in range(1, m - 1):
            dp[i][0] = (M[i - 1][0] + M[i][0] + M[i + 1][0] +
                        M[i - 1][1] + M[i][1] + M[i + 1][1]) // 6
            dp[i][n - 1] = (M[i - 1][n - 1] + M[i][n - 1] + M[i + 1][n - 1] +
                            M[i - 1][n - 2] + M[i][n - 2] + M[i + 1][n - 2]) // 6
        for j in range(1, n - 1):
            dp[0][j] = (M[0][j - 1] + M[0][j] + M[0][j + 1] +
                        M[1][j - 1] + M[1][j] + M[1][j + 1]) // 6
            dp[m - 1][j] = (M[m - 1][j - 1] + M[m - 1][j] + M[m - 1][j + 1] +
                            M[m - 2][j - 1] + M[m - 2][j] + M[m - 2][j + 1]) // 6

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                dp[i][j] = (M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][j + 1] + M[i][j - 1] +
                            M[i][j] + M[i][j + 1] + M[i + 1][j - 1] + M[i + 1][j] + M[i + 1][j + 1]) // 9
        return dp

        # 人家的解法
        # m = len(M)
        # n = len(M[0])
        # N = [[0 for j in range(n)] for i in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         count = 1
        #         N[i][j] = M[i][j]
        #         if i - 1 >= 0 and j - 1 >= 0:
        #             N[i][j] += M[i - 1][j - 1]  # 1
        #             count += 1
        #         if i - 1 >= 0 and j + 1 < n:
        #             N[i][j] += M[i - 1][j + 1]  # 3
        #             count += 1
        #         if j - 1 >= 0:
        #             N[i][j] += M[i][j - 1]  # 4
        #             count += 1
        #         if j + 1 < n:
        #             N[i][j] += M[i][j + 1]  # 5
        #             count += 1
        #         if i + 1 < m and j + 1 < n:
        #             N[i][j] += M[i + 1][j + 1]  # 8
        #             count += 1
        #         if i + 1 < m and j - 1 >= 0:
        #             N[i][j] += M[i + 1][j - 1]  # 6
        #             count += 1
        #         if i + 1 < m:
        #             N[i][j] += M[i + 1][j]  # 7
        #             count += 1
        #         if i - 1 >= 0:
        #             N[i][j] += M[i - 1][j]  # 2
        #             count += 1
        #         N[i][j] //= count
        # return N


print(Solution().imageSmoother([[1, 1, 1],
                                [1, 0, 1],
                                [1, 1, 1]]))
