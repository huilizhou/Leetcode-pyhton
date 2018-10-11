class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list1 = []
        dic1 = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in dic1:
                list1.append(dic1[c])
            elif (not list1 or c != list1.pop()):
                return False
        return not list1

        # 大神GitHub的解法。
        # stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        # for parenthese in s:
        #     if parenthese in lookup:
        #         stack.append(parenthese)
        #     elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
        #         return False
        # return len(stack) == 0


print(Solution().isValid("{}[]()"))
