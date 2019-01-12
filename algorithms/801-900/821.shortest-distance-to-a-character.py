# 字符最短的距离
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = [0] * len(S)
        currentPosition = -len(S)
        for i in range(len(S)):
            if S[i] == C:
                currentPosition = i
            res[i] = i - currentPosition
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                currentPosition = i
            res[i] = min(res[i], abs(currentPosition - i))
        return res


print(Solution().shortestToChar(S="loveleetcode", C='e'))
