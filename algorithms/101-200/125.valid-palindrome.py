# 验证回文串
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 我的解法
        res = []
        string = "qwertyuiopasdfghjklzxcvbnm0123456789"
        for i in s.lower():
            # if (48 <= ord(i) <= 57) or (97 <= ord(i) <= 122):
            if i in string:
                res.append(i)
        return res == res[::-1]

        # 人家的写法更简洁
        # s = list(filter(str.isalnum, s.lower()))  # 相等返回Trued,不相等返回False
        # return s == s[::-1]

        # 官方给的解题思路
        # n = len(s)
        # i = 0
        # j = n - 1

        # while i < j:
        #     if s[i].isalnum() == False:
        #         i += 1
        #         continue
        #     if s[j].isalnum() == False:
        #         j -= 1
        #         continue
        #     if s[i].lower() != s[j].lower():
        #         return False
        #     i += 1
        #     j -= 1
        # return True


print(Solution().isPalindrome("race a car"))
