# 丑数ii
class Solution:
    # ugly = sorted(2**a * 3**b * 5**c
    #               for a in range(32) for b in range(20) for c in range(14))

    # def nthUglyNumber(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     return self.ugly[n - 1]

    # 人家的解法
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [1]
        a, b, c = 0, 0, 0
        x, y, z = 2, 3, 5
        i = 1
        while i < n:
            p = min(x, y, z)
            t.append(p)
            if x == p:
                a += 1
                x = t[a] << 1
            if y == p:
                b += 1
                y = t[b] * 3
            if z == p:
                c += 1
                z = t[c] * 5
            i += 1

        return t[-1]


print(Solution().nthUglyNumber(10))
