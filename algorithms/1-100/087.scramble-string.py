# 扰乱字符串
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m = len(s1)
        if len(s1) < 4 and sorted(s1) == sorted(s2):
            return True
        for i in range(m - 1):
            a = sorted(s1[:i + 1]) == sorted(s2[-i - 1:]
                                             ) and sorted(s1[i + 1:]) == sorted(s2[:-i - 1])
            b = sorted(s1[:i + 1]) == sorted(s2[:i + 1]
                                             ) and sorted(s1[i + 1:]) == sorted(s2[i + 1:])
            if b and self.isScramble(s1[:i + 1], s2[:i + 1]) and self.isScramble(s1[i + 1:], s2[i + 1:]):
                return True
            if a and self.isScramble(s1[:i + 1], s2[-i - 1:]) and self.isScramble(s1[i + 1:], s2[:-i - 1]):
                return True
        return False


print(Solution().isScramble(s1="great", s2="rgeat"))
