# 字母异位词分组
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # # 使用哈希表，键值为排序后的字母异位词
        dic = {}
        for x in strs:
            sorted_x = "".join(sorted(x))
            if sorted_x in dic:
                dic[sorted_x].append(x)
            else:
                dic[sorted_x] = [x]
        return list(dic.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
