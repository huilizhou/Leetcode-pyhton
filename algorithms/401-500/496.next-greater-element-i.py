# 下一个更大元素i
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        给定两个数组，第一个数组是第二个数组的子集，说明第一个数组里面的元素都在第二个数组里面；
        依次扫描第一个数组里面的元素，去第二个数组里面找到第一个比此数大的数，存储；
        如果没有比此数大的数，则存储-1；最后输出的结果的长度一定是和第一个数组大小相等
        '''
        # 我的想法
        # for i in range(len(findNums)):
        #     position = nums.index(findNums[i])
        #     for j in range(position + 1, len(nums)):
        #         if nums[j] > findNums[i]:
        #             findNums[i] = nums[j]
        #             break
        #     if findNums[i] == nums[position]:
        #         findNums[i] = -1
        # return findNums

        # # 人家的解法
        '''
        因为第一个数组里面的元素一定在第二个元素里，所以对第二个数组进行处理；
        利用栈的知识，依次让第二个数组里的元素入栈，如果碰到要入栈的数比栈顶元素大的情况；
        我们将此时比栈顶大的数作为‘值’，此时的栈顶作为‘键’存储到hashMap中，并将这个大的数入栈；
        最后依次循环直至完成遍历第二个数组。
        这样存储键值是比较第一个数组和第二个数组里面的元素，直至在第二个数组里面找到比第一个数组小的元素，找不到则输出-1.
        '''
        # # 创建一个 哈希表 用来存储 nums 列表中的每一个数下一个比它大的数
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
