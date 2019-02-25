# 下一个更大的元素II
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 人家的解法，利用单调栈解决问题
        '''
        直接将nums复制两倍，索引的话循环的写入。
        判断栈顶元素和当前元素的大小：
        若栈顶元素>当前元素；当前元素入栈
        若栈顶元素<当前元素；弹出栈顶元素，并记录栈顶元素的下一个更大元素为当前元素。
        '''
        # res = [-1] * len(nums)
        # stack = []
        # for i in list(range(len(nums))) * 2:
        #     while stack and nums[stack[-1]] < nums[i]:
        #         res[stack.pop()] = nums[i]
        #     stack.append(i)
        # return res

        # 人家的解法
        if not nums:
            return []
        pos = nums.index(max(nums))
        stack = []
        for i in range(pos, pos - len(nums), -1):
            temp = nums[i]
            while stack:
                if stack[-1] > nums[i]:
                    nums[i] = stack[-1]
                    break
                else:
                    stack.pop()
            if not stack:
                nums[i] = -1
            stack.append(temp)
        return nums


print(Solution().nextGreaterElements([1, 2, 1]))
