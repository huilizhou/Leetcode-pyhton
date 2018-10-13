class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 人家的解法
        last, i, j = m + n - 1, m, n
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                last, i = last - 1, i - 1
            else:
                nums1[last] = nums2[j]
                last, j = last - 1, j - 1

        while j >= 0:
            nums1[last] = nums2[j]
            last, j = last - 1, j - 1

        # 我的想法,多开辟了空间，空间复杂度大一点。
        # nums = nums1[0:m]
        # for i in range(0, n):
        #     nums.append(nums2[i])
        # nums.sort()
        # for j in range(m + n):
        #     nums1[j] = nums[j]
