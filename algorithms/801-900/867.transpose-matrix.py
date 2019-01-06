class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # 我的想法
        # ret = []
        # for _ in range(len(A[0])):
        #     ret.append([])

        # for row in A:
        #     for j in range(len(A[0])):
        #         ret[j].append(row[j])
        # return ret

        # 别人的代码
        # return list(map(list,zip(*A)))

        # 官方例程，直接复制
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans


print(Solution().transpose([[1, 2, 3], [4, 5, 6]]))
