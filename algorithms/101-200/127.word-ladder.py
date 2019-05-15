class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        if beginWord in wordList:
            wordList.remove(beginWord)
        res, forword, backword = 2, {beginWord}, {endWord}
        letters, length = set('qwertyuiopasdfghjklzxcvbnm'), len(endWord)
        while forword:
            if len(forword) > len(backword):
                forword, backword = backword, forword
            cur = set()
            for word in forword:
                for idx in range(length):
                    x, y = word[:idx], word[idx + 1:]
                    for letter in letters:
                        temp = x + letter + y
                        if temp in backword:
                            return res
                        if temp in wordList:
                            cur.add(temp)
                            wordList.remove(temp)
            res += 1
            forword = cur
        return 0


print(Solution().ladderLength(beginWord="hit", endWord="cog",
                              wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
