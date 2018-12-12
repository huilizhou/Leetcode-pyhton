class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return s
        s = list(s)
        lib = "aeiouAEIOU"
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] not in lib:
                left += 1
            elif s[right] not in lib:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)


print(Solution().reverseVowels("hello"))
