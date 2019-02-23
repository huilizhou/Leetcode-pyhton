# 下一个更大元素i
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i in range(len(findNums)):
        #     position = nums.index(findNums[i])
        #     for j in range(position + 1, len(nums)):
        #         if nums[j] > findNums[i]:
        #             findNums[i] = nums[j]
        #             break
        #     if findNums[i] == nums[position]:
        #         findNums[i] = -1
        # return findNums

        # 人家的解法
        # 创建一个 哈希表 用来存储 nums 列表中的每一个数下一个比它大的数
        hash_map = dict()
        # 创建一个 栈 用来存储 nums 的栈顶
        stack = nums[0:1]

        # 对 nums 中每个数进行遍历
        # 若是后面存在比它大，则把栈顶推出
        for num in nums[1:]:
            while stack and stack[-1] < num:
                hash_map[stack.pop()] = num
            stack.append(num)
        return [hash_map.get(num, -1) for num in findNums]


print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
