#  分糖果
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        '''
        先给每人一颗糖，初始化temp数组为额外糖果。从左向右遍历，如果i+1分数高，那么dp[i+1]=dp[i]+1
        再从后往前遍历，如果i比i+1分数高，那么比较dp[i]和dp[i+1]+1,如果dp[i]小则更新。
        '''
        res = 0
        n = len(ratings)
        dp = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dp[i] = max(dp[i], dp[i + 1] + 1)
        res += sum(dp)
        return res


print(Solution().candy([1, 2]))
