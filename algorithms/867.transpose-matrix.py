class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        for _ in range(len(A[0])):
            ret.append([])

        for row in A:
            for j in range(len(A[0])):
                ret[j].append(row[j])
        return ret

        # 别人的代码
        # return list(map(list,zip(*A)))


print(Solution().transpose([[1, 2, 3], [4, 5, 6]]))
