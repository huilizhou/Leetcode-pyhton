# 组合总和II
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    #     result = []
    #     self.combinationSumRecu(sorted(candidates), result, 0, [], target)
    #     return result

    # def combinationSumRecu(self, candidates, result, start, intermediate, target):
    #     if target == 0:
    #         result.append(list(intermediate))
    #     prev = 0
    #     while start < len(candidates) and candidates[start] <= target:
    #         if prev != candidates[start]:
    #             intermediate.append(candidates[start])
    #             self.combinationSumRecu(
    #                 candidates, result, start + 1, intermediate, target - candidates[start])
    #             intermediate.pop()
    #             prev = candidates[start]
    #         start += 1

        # 回溯法求解
        result = []
        candidates.sort()
        self._combinationSum2(candidates, target, 0, list(), result)
        return result

    def _combinationSum2(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        if path and target < path[-1]:
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self._combinationSum2(
                nums, target - nums[i], i + 1, path + [nums[i]], res)


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
