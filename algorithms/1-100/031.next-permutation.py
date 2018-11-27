class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # k, l = -1, 0
        # for i in range(len(nums) - 1):
        #     if nums[i] < nums[i + 1]:
        #         k = i

        # if k == -1:
        #     nums.reverse()
        #     return

        # for i in range(k + 1, len(nums)):
        #     if nums[i] > nums[k]:
        #         l = i

        # nums[k], nums[l] = nums[l], nums[k]
        # nums[k + 1:] = nums[:k:-1]

        # 人家的解法 升序倒置法
        # 先找到从后向前数，第一个降序的位置，把此位置后面的翻转。
        # 再把这个降序数字和后面第一个比它大的交换位置即可。
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        nums[i:len(nums)] = sorted(nums[i:len(nums)])

        if i > 0:
            j = i
            i -= 1
            while j < len(nums) - 1 and nums[i] >= nums[j]:
                j += 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
