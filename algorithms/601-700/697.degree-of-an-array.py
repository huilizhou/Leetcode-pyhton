class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我的解法，有误20180922
        # res = []
        # s = {}
        # for i in nums:
        #     if i not in s:
        #         s[i] = 1
        #     else:
        #         s[i] += 1

        # max_value = max(s.values())

        # for key, value in s.items():
        #     if value == max_value:
        #         res.append(key)
        # return len(res)

        # 人家的解法
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        vmax = max(dic.values())
        if vmax == 1:
            return 1

        max_nums = []
        for i in dic.keys():
            if dic[i] == vmax:
                max_nums.append(i)

        res = len(nums)
        for i in max_nums:
            res = min(len(nums) - nums[:: -1].index(i) - nums.index(i), res)

        return res


print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
