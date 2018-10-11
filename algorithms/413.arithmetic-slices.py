class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 动态规划题目，暂时20180920不会
        if len(A) < 3:
            return 0
        else:
            num = [0 for i in range(len(A))]
            num[0], num[1] = 0, 0
            for i in range(2, len(A)):
                if 2 * A[i - 1] == A[i] + A[i - 2]:
                    num[i] = num[i - 1] + 1
            return sum(num)

        # 人家的解法
        # res, i = 0, 0
        # while i+2 < len(A):
        #     start = i
        #     while i+2 < len(A) and A[i+2] + A[i] == 2*A[i+1]:
        #         res += i - start + 1
        #         i += 1
        #     i += 1
        # return res


print(Solution().numberOfArithmeticSlices(A=[1, 2, 3, 4]))
