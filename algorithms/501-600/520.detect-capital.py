class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 我的解法。直接根据题意来考虑
        if word == word.upper() or word == word.lower() or word == word.title():
            return True
        else:
            return False

        # return word == word.upper() or word == word.lower() or word == word.title()
