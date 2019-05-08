# 猜数字游戏
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # 人家的解法
        a, b = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
        for i in range(10):
            b += min(secret.count(str(i)), guess.count(str(i)))
        return str(a) + "A" + str(b - a) + "B"


print(Solution().getHint(secret="1807", guess="7810"))
