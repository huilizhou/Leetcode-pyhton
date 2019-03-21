# 组合总和
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = self.dfs(candidates, target)
        return res

    def dfs(self, candidates, target):
        res = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            if candidates[i] == target:
                res.append([candidates[i]])
            for item in self.dfs(candidates[i:], target - candidates[i]):
                res.append([candidates[i]] + item)
        return res

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


if __name__ == "__main__":
    candidates, target = [1, 2, 5, 10, 20, 50, 100], 100
    result = Solution().combinationSum(candidates, target)
    print(result)
