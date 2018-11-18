class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 我的想法，根据题意，直接分奇偶，空间复杂度高。
        ret = []
        odd = []
        even = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        ret = even + odd
        return ret

        # # 人家的解法，一句话
        # return[i for i in A if i % 2 == 0] + [i for i in A if i % 2 == 1]


print(Solution().sortArrayByParity([3, 1, 2, 4]))
