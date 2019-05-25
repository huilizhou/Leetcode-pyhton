class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        res = ""
        while N:
            tmp = N % 2
            res = str(tmp) + res
            N = -1 * (N // 2)

        return res if res else "0"


print(Solution().baseNeg2(2))
