class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 我的想法，将其排序后比较即可
        # s = list(s)
        # s.sort()
        # t = list(t)
        # t.sort()
        # return s == t

        # 人家的解法
        if len(s) != len(t):
            return False
        for word in set(s):
            if s.count(word) != t.count(word):
                return False
        return True


print(Solution().isAnagram(s="anagram", t="nagaram"))
