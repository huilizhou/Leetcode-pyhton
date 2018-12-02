# 字母异位词分组
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # import collections
        # anagrams_map, result = collections.defaultdict(list), []
        # for s in strs:
        #     sorted_str = ("").join(sorted(s))
        #     anagrams_map[sorted_str].append(s)
        # for anagram in anagrams_map.values():
        #     anagram.sort()
        #     result.append(anagram)
        # return result

        # 人家的解法，厉害
        str_map = {}
        res = []
        for i in strs:
            string = ''.join(sorted(i))
            if string not in str_map:
                str_map[string] = len(res)
                res.append([i])
            else:
                res[str_map[string]].append(i)
        return res


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
