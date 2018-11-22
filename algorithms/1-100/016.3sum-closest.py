# 最接近的三数之和
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 我的想法
        nums.sort()
        closestnum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, r = i + 1, len(nums) - 1
            while(j < r):
                three_num = nums[i] + nums[j] + nums[r]
                if abs(three_num - target) < abs(closestnum - target):
                    closestnum = three_num
                if three_num > target:
                    r -= 1
                elif three_num < target:
                    j += 1
                else:
                    return target
        return closestnum

        # 人家的解法
        # 先判断最大的三个数是否小于target,若小于则直接返回最大的三个数
        # 再判断最小的三个数是否大于target,若大于则直接返回最小的三个数
        # 最后再判断target在这些之间。对result进行排序后取最小的值。

        # nums.sort()
        # length = len(nums)
        # result = []
        # for i, num in enumerate(nums[0:-2]):
        #     l, r = i + 1, length - 1
        #     if num + nums[r] + nums[r - 1] < target:
        #         result.append(num + nums[r] + nums[r - 1])
        #     elif num + nums[l] + nums[l + 1] > target:
        #         result.append(num + nums[l] + nums[l + 1])
        #     else:
        #         while l < r:
        #             result.append(num + nums[l] + nums[r])
        #             if num + nums[l] + nums[r] < target:
        #                 l += 1
        #             elif num + nums[l] + nums[r] > target:
        #                 r -= 1
        #             else:
        #                 return target
        # result.sort(key=lambda x: abs(x - target))
        # return result[0]


print(Solution().threeSumClosest(nums=[-1, 2, 1, -4, -2],  target=1))
