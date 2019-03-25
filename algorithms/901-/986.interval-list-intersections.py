# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """

        '''
        归并区间
        对于一个区间[a,b]，我们称b为末端点。
        在两个数组给定的所有区间中，考虑拥有最末端点的区间A[0]。（为了不失一般性，假设A[0]出现在数组A中）
        然后，在数组B的区间中，A[0]只可能与数组B中的至多一个区间相交。（如果B中存在两个区间均与A[0]相交，
        那么它们将共同包含A[0]的末端点，但是B中的区间应该是不相交的，所以导出矛盾）

        算法：
        如果A[0]拥有最小的末端点，那么它只可能与B[0]相交，然后我们可以删除区间A[0]了。因为它不能与其他区间再相交
        '''
        # 人家的想法
        # ans = []
        # i = j = 0

        # while i < len(A) and j < len(B):
        #     lo = max(A[i].start, B[j].start)
        #     hi = min(A[i].end, B[j].end)
        #     if lo <= hi:
        #         ans.append(Interval(lo, hi))

        #     if A[i].end < B[j].end:
        #         i += 1
        #     else:
        #         j += 1
        # return ans

        # 我的想法
        ans = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            left_a, right_a = A[i].start, A[i].end
            left_b, right_b = B[j].start, B[j].end
            if left_a < left_b:
                left = left_b
            else:
                left = left_a
            if right_a < right_b:
                right = right_a
                i += 1
            else:
                right = right_b
                j += 1
            if right >= left:
                ans.append(Interval(left, right))
        return ans


if __name__ == "__main__":
    A = [Interval(0, 2), Interval(5, 10)]
    B = [Interval(1, 2), Interval(5, 5)]
    print(Solution().intervalIntersection(A, B))
