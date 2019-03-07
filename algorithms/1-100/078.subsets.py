# 子集
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 人家的解法，不断遍历
        res = [[]]
        for num in nums:
            for temp in res[:]:
                x = temp[:]
                x.append(num)
                res.append(x)
        return res

        # 另一种思路，类似于二叉树的先序遍历
    #     self.results = []
    #     self.search(sorted(nums), [], 0)
    #     return self.results

    # def search(self, nums, S, index):
    #     if index == len(nums):
    #         self.results.append(S)
    #         return

    #     self.search(nums, S + [nums[index]], index + 1)
    #     self.search(nums, S, index + 1)

        # res = [[]]
        # for n in nums:
        #     res += [item + [n] for item in res]
        # return res


print(Solution().subsets([1, 2, 3]))
