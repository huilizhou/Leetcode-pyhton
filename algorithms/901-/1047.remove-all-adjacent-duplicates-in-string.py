# 删除字符串中的所有相邻重复项
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        # stack = []
        # for i in S:
        #     if not stack:
        #         stack.append(i)
        #     elif i == stack[-1]:
        #         stack.pop()
        #     else:
        #         stack.append(i)
        # return "".join(stack)

        stack = []
        for i in S:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)


print(Solution().removeDuplicates("abbaca"))
