#  每日温度
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # # 入栈条件：当前元素比栈顶元素小，出栈条件：遇到比自己大的温度，出栈时索引距离即天数差

        # stack = []
        # ret = [0] * len(T)
        # for i in range(len(T)):
        #     while stack and T[stack[-1]] < T[i]:
        #         ret[stack[-1]] = i - stack[-1]
        #         stack.pop()
        #     stack.append(i)
        # return ret

        stack = []
        ret = [0] * len(T)
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < T[i]:
                ret[stack.pop()] = i - stack[-1]
            stack.append(i)
        return ret


print(Solution().dailyTemperatures(
    [73, 74, 75, 71, 69, 72, 76, 73]))
