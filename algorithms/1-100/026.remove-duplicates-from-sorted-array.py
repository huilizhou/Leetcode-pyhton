# 删除排序数组的重复项并返回长度


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 双指针法
        '''
        数组完成排序后，我们可以放置两个指针i和j，其中i是慢指针，而j是快指针。
        只要nums[i]=nums[j]，我们就增加j以跳过重复项。
        '''
        if not nums:
            return
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


print(Solution().removeDuplicates(nums=[0, 1, 1, 2]))
