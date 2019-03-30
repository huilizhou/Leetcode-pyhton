class Solution:
    def test(self, N):
        # need = 1024 - N
        # need_64 = need // 64
        # a = need % 64
        # need_16 = a // 16
        # b = a % 16
        # need_4 = b // 4
        # c = b % 4
        # need_1 = c // 1
        # # print(need_64, need_16, need_4, need_1)
        # return (need_64 + need_16 + need_4 + need_1)
        n, answer = 1024 - N, 0
        for coin in [64, 16, 4, 1]:
            answer += n // coin
            n = n % coin
        return answer


if __name__ == "__main__":
    # N = int(input())
    print(Solution().test(200))
