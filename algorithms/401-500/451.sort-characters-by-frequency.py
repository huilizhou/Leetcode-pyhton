# 根据字符出现频率排序
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dic = {}
        # res = ''
        # for i in s:
        #     if i in dic:
        #         dic[i] += 1
        #     else:
        #         dic[i] = 1
        # while dic:
        #     tmp = max(dic, key=dic.get)
        #     res += tmp * dic[tmp]
        #     dic.pop(tmp)
        # return res

        # 人家的解法
        import collections
        cn = collections.Counter(s)
        res = ""
        for k, v in cn.most_common():
            res += k * v
        return res


print(Solution().frequencySort("tree"))
