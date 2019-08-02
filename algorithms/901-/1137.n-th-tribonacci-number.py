# 第N个泰波那契数
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # ans = [0, 1, 1]
        # if n < 3:
        #     return ans[n]
        # for i in range(3, n + 1):
        #     ans.append(ans[i - 3] + ans[i - 2] + ans[i - 1])
        # return ans[n]

        result = [0] * 38
        result[0] = 0
        result[1] = 1
        result[2] = 1
        for i in range(3, 38):
            result[i] = sum(result[i - 3:i])
        return result[n]


print(Solution().tribonacci(4))
