class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ans = list(str.strip())
        print(ans)
        if len(ans) == 0:
            return 0
        sign = -1 if ans[0] == '-' else 1
        if ans[0] in ['-', '+']:
            del ans[0]
        print(ans)
        res = 0
        i = 0
        while i < len(ans) and ans[i].isdigit():
            res = res * 10 + ord(ans[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * res, 2**31 - 1))


print(Solution().myAtoi('-32 ui'))
