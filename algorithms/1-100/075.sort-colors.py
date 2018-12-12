class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # 我的想法
        # a = nums.count(0)
        # b = nums.count(1)
        # c = nums.count(2)
        # nums[:a] = [0] * a
        # nums[a:a + b] = [1] * b
        # nums[a + b:] = [2] * c
        # return nums

        # # 人家的解法，实际上就是荷兰国旗问题。
        def triPartition(nums, target):
            i, j, n = 0, 0, len(nums) - 1

            while j <= n:
                if nums[j] < target:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[j] > target:
                    nums[j], nums[n] = nums[n], nums[j]
                    n -= 1
                else:
                    j += 1

        triPartition(nums, 1)


print(Solution().sortColors([2, 0, 2, 1, 1, 0]))
