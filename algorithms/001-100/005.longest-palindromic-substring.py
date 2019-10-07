# 最长回文子串
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # 运用动态规划的方法，先初始化一字母和二字母的回文，再找到所有3字母的，依次类推。

        # 如果字符串长度小于2或者s等于它的倒序，则直接返回s
        if len(s) < 2 or s == s[::-1]:
            return s
        # 定义起始索引和最大回文串长度，odd为奇，even为偶
        start, max_len = 0, 1
        for i in range(1, len(s)):
            # 取i及前面的max_len+2个字符
            odd = s[i - max_len - 1:i + 1]
            # 取i及前面max_len+1个字符
            even = s[i - max_len:i + 1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
        return s[start:start + max_len]

        # if len(s) <= 1 or s == s[::-1]:
        #     return s
        # start = 0
        # max_len = 0
        # for i in range(len(s)):
        #     str1 = s[i - max_len:i + 1]
        #     str2 = s[i - max_len - 1:i + 1]

        #     if (i - max_len) >= 0 and str1 == str1[::-1]:
        #         start, max_len = i - max_len, len(str1)
        #     if (i - max_len - 1) >= 0 and str2 == str2[::-1]:
        #         start, max_len = i - max_len - 1, len(str2)
        # return s[start:start + max_len]


print(Solution().longestPalindrome('abcbdasdfkk'))
# if __name__ == "__main__":
#     import sys
#     s = input()
#     print(Solution().longestPalindrome(s))
