# 数组中重复的数据
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 我的写法，不合题意。时间复杂度上
        # dic = {}
        # res = []
        # for i in nums:
        #     dic[i] = dic.get(i, 0) + 1
        #     if dic[i] > 1:
        #         res.append(i)
        # return res

        # 人家的写法，将元素变成索引，因为题目中的范围是1<=a[i]<=n
        res = []
        for n in nums:
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] *= -1
            else:
                res.append(abs(n))
        return res


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
