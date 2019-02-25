# 下一个更大元素III
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 人家的解法
        nums = list(map(int, list(str(n))))
        start = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:  # 从后往前一直升序，找到第一个降序的
                # 如1,2,6,5,4,3，则nums[start] = 2
                start = i - 1
                break
        if start == -1:  # 整个序列降序，无下一个排列
            return -1
        for i in range(len(nums) - 1, start, -1):
            if nums[i] > nums[start]:  # 在刚刚的子序列里找到第一个大于nums[start]的
                nums[i], nums[start] = nums[start], nums[i]  # 交换
                break
        nums[start + 1:] = sorted(nums[start + 1:])
        tmp = int(''.join(list(map(str, nums))))
        return tmp if tmp <= 2 ** 31 - 1 else -1
