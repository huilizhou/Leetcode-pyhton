# 编辑距离
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        '''
        首先定义状态矩阵，dp[m][n],其中m为word1的长度+1，n为word2长度+1。+1是要考虑到如果word1或者word2为空。
        定义dp[i][j]为word1中前i个字符组成的串，与word2中前j个字符组成的串的编辑距离。
        dp[i][j] 表示word1[0:i-1]这个字符串变成word2[0:j-1]这个字符串所需要的步数。


        插入操作：在word1的前i个字符后插入一个字符，使得插入的字符等于新加入的word2[j]。
        这里要考虑清楚，插入操作对于原word1字符来说，i是没有前进的，而对于word2来说是前进了一位然后两个字符串才相等的。
        所以此时是dp[i][j]=dp[i][j-1]+1。

        删除操作：在word1的第i−1​个字符后删除一个字符，使得删除后的字符串word[:i-1]与word2[:j]相同。
        这里要考虑清楚，删除操作对于原word2字符来说，j−1​是没有前进的，而对于word1来说是删除了一位然后两个字符串才相等的。
        所以此时是dp[i][j]=dp[i-1][j]+(0 or 1)。

        替换操作：在word1的第i-1个字符串后替换一个参数，使得与word2第j-1后的数字相同，此时dp[i][j]=dp[i-1][j-1]+1
        '''
        m, n = len(word1) + 1, len(word2) + 1
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0
        for i in range(1, m):
            dp[i][0] = i
        for j in range(1, n):
            dp[0][j] = j
        for i in range(1, m):
            for j in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1
        return dp[m - 1][n - 1]


print(Solution().minDistance(word1="horse", word2="ros"))
