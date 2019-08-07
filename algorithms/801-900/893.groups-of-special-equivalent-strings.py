# 特殊等价字符串组
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = set()
        for sub in A:
            sub = ''.join(sorted(sub[::2]) + sorted(sub[1::2]))
            res.add(sub)
        return len(res)


print(Solution().numSpecialEquivGroups(
    ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]))
