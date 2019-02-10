# 按递增顺序显示卡牌
class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        n = len(deck)
        if len(deck) <= 2:
            return deck
        for i in range(2, n):
            deck.insert(n - i, deck[-1])
            deck.pop()
        return deck


print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
