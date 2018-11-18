class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # nums1_set = set(nums1)
        # nums2_set = set(nums2)
        # return list(nums1_set & nums2_set)

        # 人家的解法，把多余的元素，通过集合过滤掉之后，再转换位列表
        res = []
        for num in nums1:
            if num in nums2:
                res.append(num)
        return list(set(res))
