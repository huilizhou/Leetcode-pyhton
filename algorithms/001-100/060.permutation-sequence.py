class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 人家的解法，我暂时未想出好的解法20181206
        # 人家的解法
        # factor = [0] * n
        # factor[0] = 1
        # for i in range(1, n):
        #     factor[i] = factor[i - 1] * i
        # result = ''
        # k -= 1
        # numbers = [i for i in range(1, 10)]
        # for i in range(n - 1, -1, -1):
        #     number = k // factor[i]
        #     k %= factor[i]
        #     result += str(numbers[number])
        #     del numbers[number]
        # return result

        #  人家的解法
        FAC = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        res = 0
        k -= 1
        nums = list(range(1, n + 1))
        for i in range(n):
            cs, k = divmod(k, FAC[n - i - 1])
            res = 10 * res + nums[cs]
            del nums[cs]
        return str(res)


print(Solution().getPermutation(3, 3))
