# class Solution:
#     def test(self, N):
#         # need = 1024 - N
#         # need_64 = need // 64
#         # a = need % 64
#         # need_16 = a // 16
#         # b = a % 16
#         # need_4 = b // 4
#         # c = b % 4
#         # need_1 = c // 1
#         # # print(need_64, need_16, need_4, need_1)
#         # return (need_64 + need_16 + need_4 + need_1)
#         n, answer = 1024 - N, 0
#         for coin in [64, 16, 4, 1]:
#             answer += n // coin
#             n = n % coin
#         return answer


# if __name__ == "__main__":
#     # N = int(input())
#     print(Solution().test(200))


'''
头条第一题
有1024元，买一件东西后，找零的硬币最少是：
硬币有[1,4,16,64]四种

'''


class Solution:
    def exchange(self, N):
        dp = [float('inf')] * (1024 - N + 1)
        dp[0] = 0

        for i in range(1, 1024 - N + 1):
            for coin in [1, 4, 16, 64]:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1


if __name__ == "__main__":
    N = int(input())
    print(Solution().exchange(N))
