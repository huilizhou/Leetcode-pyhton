# 平方数之和
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 我的解法
        # import math
        # low = 0
        # high = int(math.sqrt(c))
        # res = 0
        # while low <= high:
        #     res = low * low + high * high
        #     if res == c:
        #         return True
        #     elif res > c:
        #         high -= 1
        #     else:
        #         low += 1
        # return False

        # 人家的解法
        '''
        定理：某个正整数是两平方数之和，当且仅当该正整数的所有 4k+3 型素因数的幂次均为偶数。
        任何一个正整数都可以因数分解为 c = (2^r)*(p1^n1)*(p2^n2)*...*(pk^nk)，其中p1...pk为素因数，n1...nk为因数的幂次。 
        也就是说有一个形如4k+3的素因数pi，如果ni为奇数，那它就不可能被写为两个整数的平方数之和了。
        '''
        if c <= 2:
            return True
        while c % 2 == 0:
            c = c // 2
        p = 3
        while p * p <= c:
            index = 0
            while c % p == 0:
                index += 1
                c = c // p
            if (p % 4 == 3) and (index % 2 == 1):
                return False
            p += 2
        return c % 4 == 1


print(Solution().judgeSquareSum(4))
