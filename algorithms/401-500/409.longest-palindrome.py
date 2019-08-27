# 最长回文子串
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0
        flag = 0
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for v in dic.values():
            if v % 2 == 0:
                res += v
            else:
                res += (v - 1)
                flag = 1
        return res + flag


print(Solution().longestPalindrome("abccccdd"))
