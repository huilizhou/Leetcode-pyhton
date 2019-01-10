class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 我的想法
        K = [0] + [1] * 30
        for i in range(2, len(K)):
            K[i] = K[i - 1] + K[i - 2]
        return K[N]

        # 人家的想法，通项公式
        # return int((5**0.5) * 0.2 * (((1 + 5**0.5) / 2)**N - ((1 - 5**0.5) / 2)**N))

        # 人家的写法
        # if N == 0:
        #     return 0
        # elif N == 1:
        #     return 1
        # else:
        #     return self.fib(N - 1) + self.fib(N - 2)


print(Solution().fib(30))
