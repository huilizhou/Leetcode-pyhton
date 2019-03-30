# 无重复字符的最长子串
'''
暴力法非常简单，但它太慢了
在暴力法中，我们会反复检查一个子字符串是否含有重复的字符，但这是没有必要的。
如果从索引i到j-1之间的子字符串Sij已经被检查为没有重复字符。
我们只需要检测S[j]对应的字符是否已经存在于子字符串Sij中。

我们使用hashSet作为滑动窗口，我们可以用O(1)的时间来完成对字符是否在当前字符串中的检查。
滑动窗口是数组/字符串问题中常用的抽象概念。窗口通常是数组/字符串中由开始和结束索引定义的
一系列元素的集合。

我们使用HashSet将字符存储在当前窗口中，然后我们向右滑动索引j，如果它不在HashSet中，我们会继续滑动j。
直到S[j]已经存在于HashSet中。


'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # 使用哈希表
        hash = {}
        start = 0
        max_length = 0
        for i, string in enumerate(s):
            if string in hash and start <= hash[string]:
                start = hash[string] + 1
            else:
                max_length = max(max_length, i - start + 1)
            hash[string] = i
        return max_length

        # 人家的解法类似
        # curr = []
        # max_len = 0
        # for c in s:
        #     if c in curr:
        #         index = curr.index(c)
        #         curr = curr[index + 1:]
        #         curr.append(c)
        #     else:
        #         curr.append(c)
        #         currlen = len(curr)
        #         if currlen > max_len:
        #             max_len = currlen
        # return max_len

        # char_set, start, maxlen = {}, 0, 0
        # for i, ch in enumerate(s):
        #     # 如果该字符已出现
        #     if ch in char_set:
        #         # 计算长度
        #         maxlen = max(maxlen, i - start)
        #         # 更新开头
        #         start = max(start, char_set[ch] + 1)
        #     # 如果该字符未出现
        #     char_set[ch] = i
        # return max(maxlen, len(s) - start)


print(Solution().lengthOfLongestSubstring("abcad"))
