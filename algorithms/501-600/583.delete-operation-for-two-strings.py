# 两个字符串的删除操作
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # m, n = len(word1) + 1, len(word2) + 1
        # dp = [[0] * n for _ in range(m)]
        # for i in range(1, m):
        #     dp[i][0] = i
        # for j in range(1, n):
        #     dp[0][j] = j
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if word1[i - 1] == word2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        # return dp[-1][-1]

        '''
        # 人家的解法
        最长公共子序列
        https://blog.csdn.net/hrn1216/article/details/51534607
        '''
        m, n = len(word1) + 1, len(word2) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(word1) + len(word2) - 2 * dp[-1][-1]


print(Solution().minDistance('sea', 'eat'))
