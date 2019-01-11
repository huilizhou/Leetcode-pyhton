# 增减字符串匹配
class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        r = len(S)
        l = 0
        res = []
        for i in S:
            if i is "D":
                res.append(r)
                r -= 1
            else:
                res.append(l)
                l += 1
        res.append(l)
        return res


print(Solution().diStringMatch("DDI"))
