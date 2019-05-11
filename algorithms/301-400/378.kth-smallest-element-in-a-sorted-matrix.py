class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # # 我的想法，当然没有用好每行和每列都是升序排序。
        # res = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         res.append(matrix[i][j])
        # res.sort()
        # return res[k - 1]

        '''
        人家的解法，二分查找解法
        '''
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) >> 1
            count, j = 0, len(matrix[0]) - 1
            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j + 1)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left


print(Solution().kthSmallest(matrix=[
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
], k=8))
