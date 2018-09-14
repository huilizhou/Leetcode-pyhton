class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # inc = True
        # dec = True
        # for i in range(len(A) - 1):
        #     if (inc and A[i] > A[i + 1]):
        #         inc = False
        #     if (dec and A[i] < A[i + 1]):
        #         dec = False
        #     if (not inc and not dec):
        #         break
        # return inc or dec
        return A == sorted(A) or A == sorted(A, reverse=True)


print(Solution().isMonotonic([6, 5, 4, 4]))
