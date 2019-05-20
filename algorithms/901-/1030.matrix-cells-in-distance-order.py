# 距离顺序排列矩阵单元格
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        # res = [[i, j] for i in range(R) for j in range(C)]
        # res.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        # return res

        res = []
        for i in range(R):
            for j in range(C):
                res.append((abs(i - r0) + abs(j - c0), [i, j]))
        res.sort()
        return list(item[1] for item in res)


print(Solution().allCellsDistOrder(R=2, C=2, r0=0, c0=1))
