# 找到字符串中所有字母异位词
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype:
        """
        plen = len(p)
        slen = len(s)

        scnt = [0] * 26
        pcnt = [0] * 26

        res = []
        for alpha in p:
            pcnt[ord(alpha) - ord("a")] += 1

        for end in range(slen):
            if end >= plen:
                scnt[ord(s[end - plen]) - ord("a")] -= 1
            scnt[ord(s[end]) - ord("a")] += 1
            if scnt == pcnt:
                res.append(end - plen + 1)
        return res


print(Solution().findAnagrams(s="abab", p="ab"))
