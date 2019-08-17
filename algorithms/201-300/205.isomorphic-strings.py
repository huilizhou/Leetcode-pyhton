# 同构字符串
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) != len(t):
        #     return False
        # if len(set(s)) != len(set(t)):
        #     return False
        # d = {}
        # for i in range(len(s)):
        #     if s[i] in d:
        #         if d[s[i]] != t[i]:
        #             return False
        #     else:
        #         d[s[i]] = t[i]
        # return True

        st = {}
        for s1, s2 in zip(s, t):
            if s1 in st:
                if st[s1] != s2:
                    return False
            else:
                if s2 in st.values():
                    return False
                st[s1] = s2
        return True


print(Solution().isIsomorphic(s="egg", t="add"))
