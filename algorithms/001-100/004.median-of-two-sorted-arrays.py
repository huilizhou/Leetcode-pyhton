# 寻找两个有序数组的中位数
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 我的想法
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 1:
            return nums1[len(nums1) // 2]
        else:
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2.0


print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
