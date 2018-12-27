class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):
            return False
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                d[s[i]] = t[i]
        return True


print(Solution().isIsomorphic(s="egg", t="add"))
