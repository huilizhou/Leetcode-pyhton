class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # 人家的解法
        import collections
        A_B_sum = collections.Counter(a + b for a in A for b in B)
        return sum(A_B_sum[-c - d] for c in C for d in D)

        # 官方例程的解法
        # assert(len(A) == len(B) == len(C) == len(D))

        # memo = dict()
        # for i in range(len(A)):
        #     for j in range(len(B)):
        #         if A[i] + B[j] in memo:
        #             memo[A[i] + B[j]] += 1
        #         else:
        #             memo[A[i] + B[j]] = 1

        # ret = 0
        # for i in range(len(C)):
        #     for j in range(len(D)):
        #         if -C[i] - D[j] in memo:
        #             ret += memo[-C[i] - D[j]]
        # return ret


print(Solution().fourSumCount(A=[1, 2],
                              B=[-2, -1],
                              C=[-1, 2],
                              D=[0, 2]
                              ))
