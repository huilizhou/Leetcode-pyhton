# 盛最多水的容器
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 我的想法。暴力求解，超出时间限制。
        # max_area = 0
        # i, j = 0, len(height) - 1
        # while i < j:
        #     for n in range(j):
        #         max_area = max(max_area, (j - n) * min(height[n], height[j]))
        #     j -= 1
        # return max_area

        # 最初我们考虑由最外围两条线段构成的区域，现在，为了使得面积最大化。我们需要考虑更长的两条线段之间的区域。
        # 如果我们试图将指向较长的线段的指针向较短方向移动，矩形区域的受限面积不会增加。
        # 但是，同样条件下，若我们移动较短线段的指针，尽管造成了宽度的减小，但是却有可能造成面积的增加。
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
