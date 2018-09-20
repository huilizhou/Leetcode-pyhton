class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 我的解法，统计每位2进制数中1的个数将其添加到列表中
        res = []
        for i in range(0, num + 1):
            res.append(bin(i).count('1'))
        return res

        # # 人家的解法，其中按位相交
        # ans = [0]
        # for x in range(1, num + 1):
        #     ans += ans[x & (x - 1)] + 1,
        # return ans

        # # 人家的解法2
        # res = [0]
        # while len(res) <= num:
        #     res += [x + 1 for x in res]
        # return res[:num + 1]


print(Solution().countBits(7))
