# 两地调度
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        res = 0
        diff = [0] * len(costs)
        for i in range(len(costs)):
            res += costs[i][0]
            diff[i] = costs[i][1] - costs[i][0]
        diff.sort()
        for i in range(len(costs) // 2):
            res += diff[i]
        return res


print(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
