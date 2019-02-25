# 下一个更大元素I
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
        for i in range(len(findNums)):
            pos = nums.index(findNums[i])
            for j in range(pos + 1, len(nums)):
                if nums[j] > findNums[i]:
                    findNums[i] = nums[j]
                    break
            if findNums[i] == nums[pos]:
                findNums[i] = -1
        return findNums

        # # 人家的解法
        '''
        1.先遍历大数组nums，首先将第一个元素入栈；
        2.继续遍历，当当前元素小于栈顶元素时，继续将它入栈；
        当当前元素大于栈顶元素时，栈顶元素出栈，此时应将该出栈的元素与当前元素形成key-value 键值对，
        存入hash_map中；
        3.当遍历完nums后，得到nums中元素所对应的下一个更大的hash表；
        4.遍历findNums的元素在hash_map中查找下一个更大元素，当找不到时则为-1。
        '''
        # hash_map = {}
        # stack = nums[0:1]
        # for i in range(1, len(nums)):
        #     while stack and stack[-1] < nums[i]:
        #         hash_map[stack.pop()] = nums[i]
        #     stack.append(nums[i])
        # return [hash_map.get(num, -1) for num in findNums]


print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
