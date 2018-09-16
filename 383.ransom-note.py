class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        for i in range(0, len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False
            else:
                magazine = magazine.replace(ransomNote[i], '', 1)

            return True

        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                magazine = magazine.replace(c, '', 1)
        return True

        # # 别人的解法

        # import collections
        # return not collections.Counter(ransomNote) - collections.Counter(magazine)


print(Solution().canConstruct("aa", "ab"))
