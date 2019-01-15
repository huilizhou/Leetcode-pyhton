# 打乱数组
from random import randint


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ret = self.nums.copy()
        n = len(ret)
        for i in range(n - 1):
            p = randint(i, n - 1)
            ret[i], ret[p] = ret[p], ret[i]
        return ret


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
