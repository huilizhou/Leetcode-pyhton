# 最短回文串
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 人家的解法
        # n = len(s)
        # if n == 0:
        #     return ""
        # rev_str = s[::-1]
        # count = n
        # while count > 1:
        #     if rev_str[-count:] == s[:count]:
        #         break
        #     count -= 1
        # rev_str += s[count:]
        # return rev_str

        # 人家的解题思路
        '''
        先找出左边的最长回文子串，比如aacecaaa左侧最长的回文子串就是aacecaa
        然后将右侧剩余的部分反转到原串的左侧即可。由于找到的是最长的回文子串，直接从右往左，找到第一个回文子串即可。

        '''
        r = 1
        for i in range(len(s), 0, -1):
            if s[0:i] == (s[0:i])[::-1]:
                r = i
                break
        return s[r:][::-1] + s


print(Solution().shortestPalindrome("aacecaaa"))
