# 根据字符出现频率排序
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        # # 人家的解法，用库函数
        # import collections
        # cn = collections.Counter(s)
        # res = ""
        # for k, v in cn.most_common():
        #     res += k * v
        # return res

        # 人家的解法，排序部分用桶排序。/也可以用对排序
        # import collections
        # log = dict(collections.Counter(s))
        # buckets = [[] for i in range(len(s) + 1)]  # 桶排序
        # for k, v in log.items():
        #     buckets[v].append(k * v)
        # res = ''
        # for i in buckets[::-1]:
        #     res += ''.join(i)
        # return res

        # 我的写法
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        m = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        res = ''
        for i in m:
            res += i[0] * i[1]
        return res


print(Solution().frequencySort("tree"))
