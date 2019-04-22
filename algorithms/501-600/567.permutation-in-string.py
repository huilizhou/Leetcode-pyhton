# 字符串的排列
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        '''
        判断是否包含 s1 的排列的方法：
        截取 s2 中某长度和 s1 字符串长度相等的子串，判断两者每个字符的数量是否一致即可。

        统计字符数量
        由于字符串只包含 26 个小写字母，我们可以使用 计数排序 来统计，即创建一个长度为 26 的数组，其下标 0 ~ 25 对应 a ~ z 的每个字母，其值为对应字母出现的次数。

        判断条件
        先统计 s1 的字符数量 count1，再依次统计 s2 中与之长度相等的子串的字符数量 count2，比较两者是否相同。
        '''

        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        if s1 == s2:
            return True
        s = "qwertyuioopasdfghjklzxcvbnm"
        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            dict1[s[i]] = 0
            dict2[s[i]] = 0

        for i in range(l1):
            dict1[s1[i]] += 1
            dict2[s2[i]] += 1

        if dict1 == dict2:
            return True

        for i in range(l2 - l1):
            dict2[s2[i]] -= 1
            dict2[s2[i + l1]] += 1
            if dict1 == dict2:
                return True
        return False


print(Solution().checkInclusion(s1="ab", s2="abbbb"))
