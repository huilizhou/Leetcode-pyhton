class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 我的解法
        if target not in nums:
            return -1
        else:
            return nums.index(target)

        # 二分查找的方法
        # first_num = 0
        # last_num = len(nums) - 1

        # find = False

        # while first_num < last_num and not find:
        #     mid_num = (first_num + last_num) // 2
        #     if nums[mid_num] == target:
        #         find = True
        #     else:
        #         if target < nums[mid_num]:
        #             last_num = mid_num - 1
        #         else:
        #             first_num = mid_num + 1
        # if not find:
        #     mid_num = -1
        # return mid_num


print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9))
