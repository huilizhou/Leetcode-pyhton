class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 人家的想法，排序之后再采用双指针
        nums_sort = sorted(nums)
        closestnum = nums_sort[0] + nums_sort[1] + nums_sort[2]
        for i in range(len(nums) - 2):
            j, r = i + 1, len(nums) - 1
            while(j < r):
                three_num = nums_sort[i] + nums_sort[j] + nums_sort[r]
                if abs(three_num - target) < abs(closestnum - target):
                    closestnum = three_num
                if three_num > target:
                    r -= 1
                elif three_num < target:
                    j += 1
                else:
                    return target
        return closestnum


print(Solution().threeSumClosest(nums=[-1, 2, 1, -4],  target=1))
