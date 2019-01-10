# 唯一摩尔斯密码词
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # 我的想法
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        s = 'abcdefghijklmnopqrstuvwxyz'
        d = {s[i]: code[i] for i in range(26)}
        r = []
        for word in words:
            s = ''
            for item in word:
                s += d[item]
            r.append(s)
        return len(set(r))


print(Solution().uniqueMorseRepresentations(
    words=["gin", "zen", "gig", "msg"]))
