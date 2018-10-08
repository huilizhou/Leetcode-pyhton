class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(A)):
            A[i] = A[i][::-1]
            res.append(A[i])
        for j in range(len(res)):
            for k in range(len(res[j])):
                if res[j][k] == 1:
                    res[j][k] = 0
                else:
                    res[j][k] = 1
        return res


print(Solution().flipAndInvertImage(
    [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
