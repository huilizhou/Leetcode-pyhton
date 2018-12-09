class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # 我的做法
        if target in nums:
            return True
        return False

        # 人家的解法
        # nums=list(set(nums))
        # nums.sort()
        # left=0
        # right=len(nums)-1
        # while(left<=right):
        #     mid=(left+right)//2
        #     if target==nums[mid]:
        #         return True
        #     elif target<nums[mid]:
        #         right=mid-1
        #     else:
        #         left=mid+1
        # return False


print(Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
