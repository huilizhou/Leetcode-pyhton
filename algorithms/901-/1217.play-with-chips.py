# 玩筹码
class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        count0 = 0
        count1 = 0
        for i in chips:
            if i % 2 == 0:
                count0 += 1
            else:
                count1 += 1
        return min(count0, count1)


print(Solution().minCostToMoveChips([1, 2, 3]))
