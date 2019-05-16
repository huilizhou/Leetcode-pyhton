class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, nums_of_letters = [], [], 0
        for w in words:
            if nums_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - nums_of_letters):
                    if len(cur) > 1:
                        cur[i % (len(cur) - 1)] += " "
                    else:
                        cur[0] += " "
                res.append("".join(cur))
                cur, nums_of_letters = [], 0
            cur.append(w)
            nums_of_letters += len(w)
        return res + [" ".join(cur).ljust(maxWidth)]


print(Solution().fullJustify(words=[
      "This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))
