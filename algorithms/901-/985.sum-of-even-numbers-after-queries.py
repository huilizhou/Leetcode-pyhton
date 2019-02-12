class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        S = sum(x for x in A if x % 2 == 0)
        ans = []

        for x, k in queries:
            if A[k] % 2 == 0:
                S -= A[k]
            A[k] += x
            if A[k] % 2 == 0:
                S += A[k]
            ans.append(S)

        return ans


print(Solution().sumEvenAfterQueries(
    [1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]))
