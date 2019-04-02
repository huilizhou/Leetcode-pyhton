# 跳跃游戏
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 人家的解法
        # flag_max_next = 0   # 记录当前最大跳跃到达的最远索引处
        # flag_max_curr = 0   # 记录两次跳跃之间的区间内所能跳到的最远索引处
        # step = 0
        # for i in range(len(nums)):
        #     if i > flag_max_next:   # 当索引超过flag_max_next时，说明已经到达这次跳跃的最远处
        #         step += 1
        #         flag_max_next = flag_max_curr   # 用上一个跳跃区间内所保存的最远跳跃距离更新当前最大跳跃所能到达的最远索引处
        #     flag_max_curr = max(flag_max_curr, i + nums[i])

        # return step

        # 人家的解法，贪心算法
        '''
        贪心算法，遍历元素，维护的指标为当前能够到达的最大值，
        该最大值是比较上一循环的最大值和当前根据规则做运算结果进行比较得来的。
        '''
        step = 0
        lastpos = 0
        maxpos = 0
        for i in range(len(nums)):
            if i > lastpos:
                lastpos = maxpos
                step += 1
            maxpos = max(maxpos, i + nums[i])
        return step


print(Solution().jump([2, 3, 1, 1, 4]))
