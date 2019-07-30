# 用最少数量的箭引爆气球
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n == 0:
            return 0
        points.sort(key=lambda x: x[1])

        res = 1
        end = points[0][1]
        for i in range(1, n):
            if points[i][0] > end:
                end = points[i][1]
                res += 1
        return res


print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
