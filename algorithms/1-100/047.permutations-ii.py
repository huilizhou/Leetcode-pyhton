# 全排列II
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # # 调用itertools.permutations(nums, len(nums))
        # if len(nums) <= 1:
        #     return [nums]
        # import itertools
        # return list(set(itertools.permutations(nums, len(nums))))

        # # 人家的解法
        # result = []
        # result.append([])
        # for i, num in enumerate(nums):
        #     current_result = []
        #     for item in result:
        #         for j in range(i + 1):
        #             if j > 0 and num == item[j - 1]:
        #                 break
        #             temp = item[:]
        #             temp.insert(j, num)
        #             current_result.append(temp)
        #     result = current_result
        # return result

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

        # 在046题 全排列基础上，添加了去重的步骤。
        res, used = [], []
        if len(nums) <= 1:
            return [nums]
        for i in range(len(nums)):
            num = nums[i]
            if num in used:
                continue
            else:
                used.append(num)
            newnum = nums[:i] + nums[i + 1:]
            for item in self.permuteUnique(newnum):
                res.append([num] + item)
        return res


print(Solution().permuteUnique([1, 1, 2]))
