# 重复N次的元素
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 我的想法
        for i in A:
            while A.count(i) == len(A) // 2:
                return i
