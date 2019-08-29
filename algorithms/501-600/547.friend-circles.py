# 朋友圈
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited, ans = set(), 0

        def dfs(i):
            for j in range(len(M[i])):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(len(M)):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans


print(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
