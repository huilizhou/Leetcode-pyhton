# 最长连续序列
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我的想法。算法的时间复杂度O(nlogn)，不符合题意。
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

        # # 人家的解法
        # '''
        # 先判断num-1在不在nums的序列中，如果不在，
        # 继续判断num+1在不在。

        # '''

        # longest_streak = 0
        # num_set = set(nums)

        # for num in num_set:
        #     if num - 1 not in num_set:
        #         current_num = num
        #         current_streak = 1

        #         while current_num + 1 in num_set:
        #             current_num += 1
        #             current_streak += 1

        #         longest_streak = max(longest_streak, current_streak)

        # return longest_streak

        # 人家的解法
        """
        思路如下：
        用哈希表存储每个端点值对应连续区间的长度
        若数已经在哈希表中，则跳过不处理
        若是新数加入：
            1.取其左右相邻数已有的连续区间长度left和right
            2.计算当前数的区间长度为：cur_length = left + right + 1
            3.根据 cur_length 更新最大长度 max_length 的值
            4.更新区间两端点的长度值
        """

        hash_dict = dict()
        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)

                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length

                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length

        return max_length


print(Solution().longestConsecutive([100, 4, 1, 3, 2, 5, 7, 8, 3]))
