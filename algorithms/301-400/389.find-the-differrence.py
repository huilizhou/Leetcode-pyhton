class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 我的想法，统计字母的个数，返回不同个数的字母
        for i in range(97, 123):
            if s.count(chr(i)) != t.count(chr(i)):
                return chr(i)

        # 人家的想法
        # i = 0
        # for c in s + t:
        #     i ^= ord(c)
        # return chr(i)


print(Solution().findTheDifference(s="abcd", t="abcde"))
