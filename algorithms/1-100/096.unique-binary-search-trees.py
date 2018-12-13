# 不同的二叉搜索树
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 直接根据排列组合公式求解，
        # https://zh.wikipedia.org/wiki/%E5%8D%A1%E5%A1%94%E5%85%B0%E6%95%B0
        # if n == 0:
        #     return 1

        # def combination(n, k):
        #     count = 1
        #     # C(n, k) = (n) / 1 * (n - 1) / 2 ... * (n - k + 1) / k
        #     for i in range(1, k + 1):
        #         count = count * (n - i + 1) / i
        #     return count

        # return combination(2 * n, n) - combination(2 * n, n - 1)

        # 动态规划，由状态转移方程求解。
        counts = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for j in range(i):
                count += counts[j] * counts[i - j - 1]
            counts.append(count)
        return counts[-1]


print(Solution().numTrees(3))
