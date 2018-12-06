class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 人家的解法
        flag_max_next = 0   # 记录当前最大跳跃到达的最远索引处
        flag_max_curr = 0   # 记录两次跳跃之间的区间内所能跳到的最远索引处
        step = 0
        length = len(nums)
        for i in range(length):
            if i > flag_max_next:   # 当索引超过flag_max_next时，说明已经到达这次跳跃的最远处
                step += 1
                flag_max_next = flag_max_curr   # 用上一个跳跃区间内所保存的最远跳跃距离更新当前最大跳跃所能到达的最远索引处
            flag_max_curr = max(flag_max_curr, i + nums[i])

        return step

        # jump_count = 0
        # reachable = 0
        # curr_reachable = 0
        # for i, length in enumerate(nums):
        #     if i > reachable:
        #         return -1
        #     if i > curr_reachable:
        #         curr_reachable = reachable
        #         jump_count += 1
        #     reachable = max(reachable, i + length)
        # return jump_count


print(Solution().jump([2, 3, 1, 1, 4]))
