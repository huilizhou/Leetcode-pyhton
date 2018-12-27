# 重复的DNA序列
class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 别人的解法
        # 将所有长度为10的子序列存进map中
        candiate = set()
        result = set()
        for index in range(len(s) - 9):
            ele = s[index:index + 10]
            if ele in candiate:
                result.add(ele)
            candiate.add(ele)

        return list(result)


print(Solution().findRepeatedDnaSequences(
    s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
