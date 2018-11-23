class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # # 我的想法
        # nums.sort()
        # res = []
        # for i in range(len(nums) - 3):
        #     if i and nums[i] == nums[i - 1]:
        #         continue
        #     for j in range(i + 1, len(nums) - 2):
        #         if j != i + 1 and nums[j] == nums[j - 1]:
        #             continue
        #         sum = target - nums[i] - nums[j]
        #         left, right = j + 1, len(nums) - 1
        #         while left < right:
        #             if nums[left] + nums[right] == sum:
        #                 res.append([nums[i], nums[j], nums[left], nums[right]])
        #                 right -= 1
        #                 left += 1
        #                 while left < right and nums[left] == nums[left - 1]:
        #                     left += 1
        #                 while left < right and nums[right] == nums[right + 1]:
        #                     right -= 1
        #             elif nums[left] + nums[right] > sum:
        #                 right -= 1
        #             else:
        #                 left += 1
        # return res

        def findNsum(nums, target, N):
            """
            多个数之和这一类问题的通解
            :param nums:
            :param target
            :param N
            :return 
            :notes:
            传进来的nums 已经完成了从大到小的排序
            """

            res = []
            if len(nums) < N or target < nums[0] * N or target > nums[-1] * N:
                return res

            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append([nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l, r = l + 1, r - 1
            else:
                for i, x in enumerate(nums[:-N + 1]):
                    if i == 0 or (i > 0 and nums[i - 1] != x):
                        res1 = findNsum(nums[i + 1:], target - x, N - 1)
                        if len(res1) > 0:
                            res += [[x] + y for y in res1]
            return res

        return findNsum(sorted(nums), target, 4)


print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
