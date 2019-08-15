# 全排列II
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # # 调用库函数
        # if len(nums) <= 1:
        #     return [nums]
        # import itertools
        # return list(set(itertools.permutations(nums, len(nums))))

        # 人家的解法
        # result = [[]]
        # for i, num in enumerate(nums):
        #     temp = []
        #     for res in result:
        #         for j in range(i + 1):
        #             temp.append(res[:j] + [num] + res[j:])
        #             # 插值时若与下一位相等，则接下来的位置不必再试，否则一定会出现重复
        #             if j < i and num == res[j]:
        #                 break
        #     result = temp
        # return result

        # 递归
        # res, used = [], []
        # if len(nums) <= 1:
        #     return [nums]
        # for i in range(len(nums)):
        #     num = nums[i]
        #     if num not in used:
        #         used.append(num)
        #     else:
        #         continue
        #     newnum = nums[:i] + nums[i + 1:]
        #     for item in self.permuteUnique(newnum):
        #         res.append([num] + item)
        # return res


print(Solution().permuteUnique([1, 1, 2]))
