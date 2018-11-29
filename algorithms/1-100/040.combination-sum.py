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

        # 人家的解法,DFS算法
        candidates.sort()

        def findSum(cans, tar):
            result_list = []
            i = 0
            while i < len(cans):
                can = cans[i]
                # print(cans, tar)
                can = cans[i]
                if tar == can:
                    result_list.append([can])
                elif tar > can:
                    found = findSum(cans[i + 1:], tar - can)
                    if found:
                        for sum_list in found:
                            sum_list.append(can)
                            result_list.append(sum_list)
                else:
                    return result_list
                while i < len(cans) and cans[i] == can:
                    i += 1
            return result_list
        return findSum(candidates, target)


print(Solution().combinationSum2())
