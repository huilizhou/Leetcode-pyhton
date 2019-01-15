class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda P: P[0]**2 + P[1]**2)
        return points[:K]


print(Solution().kClosest(points=[[1, 3], [-2, 2]], K=1))
