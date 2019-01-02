class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 直接转
        # return s[::-1]

        # 我的解法
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)


print(Solution().reverseString("A man, a plan, a canal: Panama"))
