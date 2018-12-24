class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        idx = 0
        while (5**idx - 1) // 4 < K:
            idx += 1
        while idx - 1 > 0:
            temp = (5**idx - 1) // 4
            while K - temp > -2:
                K -= temp
            idx -= 1
        if not K + 1:
            return 0
        return 5
