# 实现strSTR()
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 我的想法
        if not needle:
            return 0
        elif needle not in haystack:
            return -1
        elif needle in haystack:
            return haystack.find(needle)

        # for i in range(len(haystack) - len(needle) + 1):
        #     if haystack[i:i + len(needle)] == needle:
        #         return i
        # return -1


print(Solution().strStr(haystack="hello", needle="ll"))
