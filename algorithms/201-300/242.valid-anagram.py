# 有效的字母异位词
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 我的想法，将其排序后比较即可
        # return "".join(sorted(s)) == "".join(sorted(t))

        # # 人家的解法
        if len(s) != len(t):
            return False
        for word in set(s):
            if s.count(word) != t.count(word):
                return False
        return True


print(Solution().isAnagram(s="anagram", t="nagaram"))
