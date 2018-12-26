# 寻找数组的中心索引
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 人家的写法
        # if (len(nums)) < 3:
        #     return -1
        # sum_total, left = sum(nums), 0
        # for i in range(len(nums)):
        #     if (sum_total - nums[i]) / 2 == left:
        #         return i
        #     left += nums[i]
        # return -1

        # 人家的解法，思路相同
        totalSum = sum(nums)
        leftSum = 0

        for i, num in enumerate(nums):
            if leftSum == totalSum - leftSum - num:
                return i
            leftSum += num

        return -1


print(Solution().pivotIndex([1, 2, 3]))
