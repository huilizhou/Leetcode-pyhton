# 最长连续序列
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 人家的解法
        # 用hashmap来保存数组中已经遍历过的元素
        # key对应元素的值，value表示该元素所在的连续子数组的长度

        # result, lengths = 0, {key: 0 for key in nums}
        # for i in nums:
        #     if lengths[i] == 0:
        #         lengths[i] = 1
        #         left, right = lengths.get(i - 1, 0), lengths.get(i + 1, 0)
        #         length = 1 + left + right
        #         result, lengths[i - left], lengths[i +
        #                                            right] = max(result, length), length, length
        # return result

        # 人家的解法
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

        # 我的想法。算法的时间复杂度O(nlogn)
        # if not nums:
        #     return 0
        # nums.sort()
        # res = 1
        # count = 1
        # for i in range(len(nums) - 1):
        #     if nums[i + 1] == nums[i] + 1:
        #         count += 1
        #         res = max(res, count)
        #     elif nums[i + 1] == nums[i]:
        #         continue
        #     else:
        #         count = 1
        # return res


print(Solution().longestConsecutive([100, 4, 1, 3, 2, 5, 7, 8, 3]))
