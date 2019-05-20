class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        '''
        两人选择的每一步都是要考虑选择此步是否对自己有利。
        由分析可知，若N是偶数，在爱丽丝每步都是最佳状态选择的情况下，爱丽丝赢得比赛
        若N是奇数，在鲍勃以最佳状态的选择的情况下，鲍勃可以赢得比赛。
        '''
        return N % 2 == 0

        # # 人家的解法
        # dp = [0 for i in range(N + 1)]
        # dp[1] = 0
        # if N <= 1:
        #     return 0
        # dp[2] = 1
        # for i in range(3, N + 1):
        #     for j in range(1, i // 2):
        #         if i % j == 0 and dp[i - j] == 0:
        #             dp[i] = 1
        #             break
        # return dp[N] == 1


print(Solution().divisorGame(3))
