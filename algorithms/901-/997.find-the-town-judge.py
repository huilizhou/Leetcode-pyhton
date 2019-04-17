# 寻找小镇法官
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # 人家的解法
        '''
        入度+1
        出度-1
        最后若存在g[i]=N-1
        则返回索引i
        '''
        g = [0] * (N + 1)
        for t in trust:
            g[t[0]] -= 1
            g[t[1]] += 1
        for i in range(1, N + 1):
            if g[i] == N - 1:
                return i
        return -1


print(Solution().findJudge(N=3, trust=[[1, 3], [2, 3]]))
