class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSubsequence(a, b):
            i = 0
            for j in range(len(b)):
                if i >= len(a):
                    break
                if a[i] == b[j]:
                    i += 1
            return i == len(a)

        strs.sort(key=len, reverse=True)
        for i in range(len(strs)):
            all_of = True
            for j in range(len(strs)):
                if len(strs[j]) < len(strs[i]):
                    break
                if i != j and isSubsequence(strs[i], strs[j]):
                    all_of = False
                    break
            if all_of:
                return len(strs[i])
        return -1

    # 人家的解法
    # 问题等价于秋字符串数组中，最长非公共字串的长度，先找非公共子串，在找最长的。
        # def issub(s, t):
        #     t = iter(t)
        #     return all(c in t for c in s)
        # for s in sorted(strs, key=len, reverse=True):
        #     if sum(issub(s, t) for t in strs) == 1:
        #         return len(s)
        # return -1


print(Solution().findLUSlength(['abc', 'caddd', '']))
