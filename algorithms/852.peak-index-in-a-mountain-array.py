class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 我的解法，根据题意来求解
        return A.index(max(A))

        # 人家的解法,二分法

        # first = 0
        # last = len(A) - 1
        # while last - first > 1:
        #     mid = (first + last) // 2
        #     if A[mid] - A[mid - 1] > 0:
        #         first = mid
        #     else:
        #         last = mid

        # if A[first] > A[last]:
        #     result = first
        # else:
        #     result = last

        # return result


print(Solution().peakIndexInMountainArray([1, 2, 3, 1]))
