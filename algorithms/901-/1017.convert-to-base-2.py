class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        # res = ""
        # while N:
        #     tmp = N % 2
        #     res = str(tmp) + res
        #     N = -1 * (N // 2)

        # return res if res else "0"

        # 人家的解法
        if N == 0:
            return '0'
        res = ''
        while 1:
            b = N % (-2)
            if N == 1:
                res += '1'
                return res[::-1]

            if b == 0:
                res += ('0')
                N = N // (-2)
            else:
                res += ('1')
                N = N // (-2) + 1


print(Solution().baseNeg2(8))
