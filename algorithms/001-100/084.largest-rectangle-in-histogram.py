# 柱状图中面积最大的矩形
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # stack = []
        # result = 0
        # heights.append(0)
        # for i in range(len(heights)):
        #     top = i
        #     while stack != [] and heights[i] < heights[stack[-1]]:
        #         top = stack.pop()
        #         result = max((i - top) * heights[top], result)
        #     if stack == [] or heights[i] > heights[stack[-1]]:
        #         heights[top] = heights[i]
        #         stack.append(top)
        # return result

        # 暴力解，超出时间限制
        res = 0
        for i in range(len(heights)):
            min_height = float('inf')
            for j in range(i, len(heights)):
                min_height = min(heights[j], min_height)
                res = max(res, min_height * (j - i + 1))
        return res


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
