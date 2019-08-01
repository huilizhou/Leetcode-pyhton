# 判断子序列
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in s:
            if i in t:
                idx = t.index(i)
                t = t[idx + 1:]
            elif i not in t:
                return False
        return True

        """
        人家的解法
        借助迭代器和生成器
        巧妙地利用了成器的特性， next() 函数运行的时候， 保存了当前的指针。

        那么((i in b) for i in s)可以理解为：遍历s中元素 i，并在b中查找元素 i 是否存在。
        由于next() 函数和yield 生成器的特性,如果 b 存在 i 返回True并保存当前指针不存在返回False
        （下一次查找从保存的指针开始继续查找，直到s 或者 b 遍历结束），这些True或False产生一个迭代器。

        最后的 all() 函数，判断一个迭代器的元素是否全部为 True， 如果是则返回 True， 否则就返回 False。
        """
        # b = iter(t)  # 迭代器
        # return all(((i in b) for i in s))


print(Solution().isSubsequence("abc", "ahbgdc"))
