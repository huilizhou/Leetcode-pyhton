# 组合总和
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 递归的解法
    #     res = self.dfs(candidates, target)
    #     return res

    # def dfs(self, candidates, target):
    #     res = []
    #     for i in range(len(candidates)):
    #         if candidates[i] > target:
    #             continue
    #         if candidates[i] == target:
    #             res.append([candidates[i]])
    #         for item in self.dfs(candidates[i:], target - candidates[i]):
    #             res.append([candidates[i]] + item)
    #     return res

        # 我的想法，递归
        # '''
        # 我的想法递归
        # '''
        # if target < 0:
        #     return []
        # res = []
        # for i, a in enumerate(candidates):
        #     if a == target:
        #         res.append([a])
        #     for j in self.combinationSum(candidates[i:], target - a):
        #         res.append([a] + j)
        # return res

        # 回溯法求解
        result = []
        candidates.sort()
        self._combinationSum(candidates, target, 0, list(), result)
        return result

    def _combinationSum(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self._combinationSum(
                nums, target - nums[i], i, path + [nums[i]], res)


if __name__ == "__main__":
    candidates, target = [2, 6, 3, 7], 7
    result = Solution().combinationSum(candidates, target)
    print(result)
