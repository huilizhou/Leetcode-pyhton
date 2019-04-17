# 最低票价
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        '''
        如果，你不必出行的话，等一等购买火车票一定最优，如果需要出行的话，那么就有三种选择：
        在通行期为1天、7天、30天中的火车票中选择一张购买
        
        我们可以把这种选择的过程表示为递归的形式。

        dp[n]=min(dp[n-1]+costs[0],dp[n-7]+costs[1],dp[n-30]+costs[2])
        其中n>=0
        空间复杂度和时间复杂度较大
        '''
        dp = [0] * 366
        for i in range(1, 366):
            if i in days:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(i - 7, 0)] +
                            costs[1], dp[max(i - 30, 0)] + costs[2])
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


print(Solution().mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
