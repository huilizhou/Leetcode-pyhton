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

        # 分别比较字母的个数
        # if len(s) != len(t):
        #     return False
        # for word in set(s):
        #     if s.count(word) != t.count(word):
        #         return False
        # return True

        # 解法
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for j in t:
            dic[j] = dic.get(j, 0) - 1
        for v in dic.values():
            if v != 0:
                return False
        return True


print(Solution().isAnagram(s="anagram", t="nagaram"))
