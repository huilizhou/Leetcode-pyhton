# 加油站
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 我的想法
        '''
        gas[i]-cost[i]+temp>=0 才可以继续走
        否则的话，则不行。
        初始起点为0，由题意知，如果有解，则为唯一解。
        '''
        if sum(gas) < sum(cost):
            return -1

        index = 0
        temp = 0
        for i in range(len(gas)):
            if gas[i] - cost[i] + temp >= 0:
                temp += gas[i] - cost[i]
            else:
                temp = 0
                index = i + 1
        return index

        # # 人家的解法
        # n = len(gas)
        # min_val = 0
        # cur = 0
        # start = 0
        # for i in range(n):
        #     cur = cur + gas[i] - cost[i]
        #     if cur < min_val:
        #         min_val = cur
        #         start = i + 1
        # if cur < 0:
        #     return -1
        # else:
        #     return start


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
