class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        '''
        左神的解法，看得明白。没有压缩空间，可以改进
        '''
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            if s1[i - 1] != s3[i - 1]:
                break
            dp[i][0] = True
        for j in range(1, len(s2) + 1):
            if s2[j - 1] != s3[j - 1]:
                break
            dp[0][j] = True
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                elif s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
        return dp[-1][-1]


print(Solution().isInterleave(s1="aa", s2="ab", s3="aaba"))
