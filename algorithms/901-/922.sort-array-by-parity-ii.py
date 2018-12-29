class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 我的想法
        res = [0] * len(A)
        i, j = 0, 1
        for k in range(len(A)):
            if A[k] % 2 == 0:
                res[i] = A[k]
                i += 2
            else:
                res[j] = A[k]
                j += 2
        return res


print(Solution().sortArrayByParityII([4, 2, 5, 7]))
