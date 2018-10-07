class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 我的想法，和349题类似的。
        res = []
        for num in nums1:
            if num in nums2:
                res.append(num)
                nums2.remove(num)
        return res


print(Solution().intersect([1, 2, 2, 1], [2]))
