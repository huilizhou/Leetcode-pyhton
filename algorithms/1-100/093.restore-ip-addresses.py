class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # IP地址分为四个小段，每一小段都是在0~255这个区间内（第一小段不能为0）
        # 人家的解法
    #     result = []
    #     self.restoreIpAddressesRecur(result, s, 0, "", 0)
    #     return result

    # def restoreIpAddressesRecur(self, result, s, start, current, dots):
    #     # pruning to improve performance
    #     if (4 - dots) * 3 < len(s) - start or (4 - dots) > len(s) - start:
    #         return

    #     if start == len(s) and dots == 4:
    #         result.append(current[:-1])
    #     else:
    #         for i in range(start, start + 3):
    #             if len(s) > i and self.isValid(s[start:i + 1]):
    #                 current += s[start:i + 1] + '.'
    #                 self.restoreIpAddressesRecur(
    #                     result, s, i + 1, current, dots + 1)
    #                 current = current[:-(i - start + 2)]

    # def isValid(self, s):
    #     if len(s) == 0 or (s[0] == '0' and s != "0"):
    #         return False
    #     return int(s) < 256

        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append(".".join(path))
            return
        for i in range(min(3, len(s))):
            curr = s[:i + 1]
            if(curr[0] == "0" and len(curr) <= 2) or int(curr) > 255:
                continue
            self.dfs(s[i + 1:], path + [s[:i + 1]], res)


print(Solution().restoreIpAddresses("25525511135"))
