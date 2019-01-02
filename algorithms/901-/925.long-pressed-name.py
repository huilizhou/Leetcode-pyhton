# 长按键入
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        # 人家的解法，双指针
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)

        # 我的想法
        # i, j = 0, 0
        # n, m = len(name), len(typed)
        # last = None
        # while i < n and j < m:
        #     if name[i] == typed[j]:
        #         last = name[i]
        #         i += 1
        #         j += 1
        #     elif typed[j] == last:
        #         j += 1
        #     else:
        #         return False
        # while j < m and typed[j] == last:
        #     j += 1
        # return i == n and j == m


print(Solution().isLongPressedName(name="alex", typed="aallex"))
