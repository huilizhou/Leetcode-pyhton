# 最后一块石头的重量
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.pop(-1)
                stones.pop(-1)
            else:
                stones[-1] = stones[-1] - stones[-2]
                stones.pop(-2)
        if len(stones) != 0:
            return stones[0]
        else:
            return 0


print(Solution().lastStoneWeight(
    [2, 7, 4, 1, 8, 1]))
