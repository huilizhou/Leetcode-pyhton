class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            count += (ord(s[i]) - 64) * 26**(len(s) - 1 - i)
        return count


print(Solution().titleToNumber("AB"))
