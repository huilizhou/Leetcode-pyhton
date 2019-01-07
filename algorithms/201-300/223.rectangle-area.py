# 矩形面积
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # 我的写法
        # area1 = (C - A) * (D - B)
        # area2 = (G - E) * (H - F)
        # ma = max(A, E)
        # mb = min(C, G)
        # l1 = mb - ma
        # if l1 <= 0:
        #     return area1 + area2

        # mc = max(B, F)
        # md = min(D, H)
        # l2 = md - mc

        # if l2 <= 0:
        #     return area1 + area2

        # return area1 + area1 - l1 * l2

        # 人家的解法
        return (C - A) * (D - B) + (G - E) * (H - F) - max(0, min(C, G) - max(A, E)) * max(0, min(D, H) - max(B, F))


print(Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
