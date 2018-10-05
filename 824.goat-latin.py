class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = S.split()
        A = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(s)):
            if s[i][0] in A:
                s[i] += 'ma' + 'a' * (i + 1)
            else:
                s[i] = s[i][1:] + s[i][0] + 'ma' + 'a' * (i + 1)
        return ' '.join(s)


print(Solution().toGoatLatin(
    "Each word consists of lowercase and uppercase letters only"))
