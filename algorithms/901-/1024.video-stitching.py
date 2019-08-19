class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        dp = [T + 1] * (T + 1)
        dp[0] = 0
        for i in range(0, T + 1):
            for c in clips:
                if c[0] <= i and c[1] >= i:
                    dp[i] = min(dp[i], dp[c[0]] + 1)
        return -1 if dp[T] == T + 1 else dp[T]


print(Solution().videoStitching(
    [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
