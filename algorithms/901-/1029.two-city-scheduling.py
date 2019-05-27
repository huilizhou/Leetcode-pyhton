# 两地调度
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        '''
        第一步：先所有人都去A市，此时记录B市与A市的差价
        第二步：将B与A的差价按从小到达排序。
        第三步：所有的值加上一半的差价前面的值。

        '''
        # res = 0
        # diff = [0] * len(costs)
        # for i in range(len(costs)):
        #     res += costs[i][0]
        #     diff[i] = costs[i][1] - costs[i][0]
        # diff.sort()
        # for i in range(len(costs) // 2):
        #     res += diff[i]
        # return res

        # 人家的解法
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        res, n = 0, len(costs) // 2
        for i in range(n):
            res += costs[i][0] + costs[i + n][1]
        return res


print(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
