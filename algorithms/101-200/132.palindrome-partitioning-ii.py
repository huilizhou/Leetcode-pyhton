# 分割回文串
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[i - 1::-1] and s[i:] == s[:i - 1:-1]:
                return 1
        if not s:
            return 0

        dp = [i for i in range(-1, len(s))]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]


print(Solution().minCut("aab"))
