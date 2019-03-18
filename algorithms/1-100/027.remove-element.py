class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # while val in nums:
        #     nums.remove(val)
        # return len(nums)

        # 人家的解法
        '''
        双指针，既然问题要我们就地删除给定值的所有元素，我们就必须使用O(1)的额外空间来处理它。
        我们可以保留两个指针i和j，其中i是慢指针，j是快指针。
        当nums[j]与给定值相等的时候，递增j以跳过该元素，只要nums[j]不等于val，我们就复制nums[j]到
        nums[i]并同时递增两个索引。重复这一过程，直到j到达数组的末尾。
        '''
        n = len(nums)
        i = -1
        j = 0
        while j <= n - 1:
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1


print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
