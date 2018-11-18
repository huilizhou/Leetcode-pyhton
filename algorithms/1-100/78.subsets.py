class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 人家的解法，20180921不太懂，回溯法。
        # nums.sort()
        # result = [[]]
        # for i in range(len(nums)):
        #     size = len(result)
        #     for j in range(size):
        #         result.append(list(result[j]))
        #         result[-1].append(nums[i])
        # return result

        # 人家的解法，不断遍历
        res = [[]]
        for num in nums:
            for temp in res[:]:
                x = temp[:]
                x.append(num)
                res.append(x)
        return res


print(Solution().subsets([1, 2, 3]))
