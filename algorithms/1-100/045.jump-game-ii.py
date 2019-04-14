# 跳跃游戏
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 人家的解法
        '''
        贪心算法，遍历元素，维护的指标为当前能够到达的最大值，
        该最大值是比较上一循环的最大值和当前根据规则做运算结果进行比较得来的。

        左的做法

        jump 代表目前跳了多少步
        cur 代表如果只能跳jump步，最远能够到达的位置
        next 代表如果能多跳一步，最远能到达的位置
        初始状态为jump=0,cur=0,next=0

        从左到右遍历nums，假设遍历到位置i。
        如果cur>=i，说明跳jump步可以到达位置i，此时什么都不需做。
        如果cur<i，说明只跳jump步不能到达位置i，需要多跳一步才行，
        此时令jump+=1，cur=next。表示多跳了一步，cur更新成跳jump+1能够到达的位置，即next。
        将next更新为max(next,nums[i]+i)，表示下一次多跳一步到达的最远的位置。
        '''
        jump = 0
        cur = 0
        next = 0
        for i in range(len(nums)):
            if cur < i:
                jump += 1
                cur = next
            next = max(next, nums[i] + i)
        return jump


print(Solution().jump([2, 3, 1, 1, 4]))
