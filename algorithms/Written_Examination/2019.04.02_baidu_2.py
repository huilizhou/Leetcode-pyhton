class Solution:
    def test(self, distance, coins):
        dp = [0] * (distance[-1] + 1)
        coins.sort()

        dp[0] = 1
        for coin in coins:
            for i in range(coin, distance[-1] + 1):
                dp[i] = dp[i] + dp[i - coin]

        res = [distance[0]]
        for i in range(1, len(distance)):
            res.append(distance[i] - distance[i - 1])

        max = 1
        for i in res:
            max *= dp[i]
        return max


if __name__ == "__main__":
    distance = [0, 5, 10]
    coins = [1, 2, 5]
    print(Solution().test(distance, coins))
