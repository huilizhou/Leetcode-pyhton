# 数组的相对排序
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in arr2:
            res.extend([i] * arr1.count(i))

        for j in sorted(list(set(arr1) - set(arr2))):
            res.extend([j] * arr1.count(j))

        return res


print(Solution().relativeSortArray(
    arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
