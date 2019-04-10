# 分发饼干
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while(child < len(g) and cookie < len(s)):
            if (g[child] <= s[cookie]):
                child += 1
            cookie += 1
        return child


print(Solution().findContentChildren([1, 2, 3], [1, 1]))
