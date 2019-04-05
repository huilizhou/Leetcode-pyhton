# 不同的二叉搜索树
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 直接根据排列组合公式求解，
        # 卡特兰公式
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

        # 卡特兰数
        sum_1 = 1
        for i in range(n + 1, 2 * n + 1):
            sum_1 *= i
        sum_2 = 1
        for i in range(1, n + 1):
            sum_2 *= i
        return sum_1 // (sum_2 * (n + 1))

        # 动态规划，由状态转移方程求解。
        '''
        解题思路：假设n个节点存在二叉排序树的个数是G(n)，1为根结点，2为根结点，...，n为根结点。
        当1为根结点的时候，其左子树的结点个数为0，右子树结点个数为n-1。
        同理当2为根结点的时候，其左子树结点个数为1，右子树结点为n-2，所以可得
        G(n)=G(0)*G(n-1)+G(1)*G(n-2)+...+G(n-1)*G(0)
        # '''
        # counts = [1, 1]
        # for i in range(2, n + 1):
        #     count = 0
        #     for j in range(i):
        #         count += counts[j] * counts[i - j - 1]
        #     counts.append(count)
        # return counts[-1]

        # # 我的写法
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2, n + 1):
        #     for j in range(i):
        #         dp[i] += dp[j] * dp[i - j - 1]
        # return dp[-1]


print(Solution().numTrees(4))
