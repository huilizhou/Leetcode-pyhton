# 计算右侧小于当前元素的个数
class Solution(object):
    # def countSmaller(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     import bisect

    #     count_list = []
    #     result_list = []
    #     nums.reverse()

    #     for i in nums:
    #         index = bisect.bisect_left(count_list, i)
    #         count_list.insert(index, i)
    #         result_list.append(index)
    #     result_list.reverse()
    #     return result_list

    # # 我的解法，有一个测试用例超时，时间复杂度为O(n^2)
    # res = []
    # if not nums:
    #     return res
    # for i in range(len(nums) - 1):
    #     count = 0
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] > nums[j]:
    #             count += 1
    #     res.append(count)
    # res.append(0)
    # return res

    def bisearch(self, tmp, a):
        left = 0
        right = len(tmp)
        while left < right:
            mid = (left + right) // 2
            if tmp[mid] < a:
                left = mid + 1
            else:
                right = mid
        return left

    def countSmaller(self, nums):
        ans = []
        tmp = []

        for i in range(len(nums) - 1, -1, -1):
            pos = self.bisearch(tmp, nums[i])
            ans.append(pos)
            tmp.insert(pos, nums[i])
        ans.reverse()
        return ans


print(Solution().countSmaller([5, 2, 6, 1]))
