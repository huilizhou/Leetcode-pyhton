# 高度检查器
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        height_sort = sorted(heights)
        res = 0
        for i, value in enumerate(heights):
            if height_sort[i] != value:
                res += 1
        return res


print(Solution().heightChecker([1, 1, 4, 2, 1, 3]))
