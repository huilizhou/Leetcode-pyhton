class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # s = list(s)
        # for i in range(0, len(s), 2*k):
        #     s[i:i+k] = reversed(s[i:i+k])
        # return "".join(s)

        l = len(s)
        res = ''
        for i in range(0, l, 2 * k):
            res += s[i:i + k][::-1] + s[i + k:i + 2 * k]
        return res


print(Solution().reverseStr('abcdefg', 2))
