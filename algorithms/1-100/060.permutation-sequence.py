class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 人家的解法，我暂时未想出好的解法20181204

        import math
        seq, k, fact = "", k - 1, math.factorial(n - 1)
        perm = [i for i in range(1, n + 1)]
        for i in reversed(range(n)):
            curr = perm[int(k / fact)]
            seq += str(curr)
            perm.remove(curr)
            if i > 0:
                k %= fact
                fact /= i
        return seq


print(Solution().getPermutation(3, 3))
