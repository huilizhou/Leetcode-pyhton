# 有问题，通过9%
a = int(input())
prices = list(map(int, input().spilt()))


res = 0
cnt = 0
for i in range(1, len(prices)):
    if prices[i] - prices[i - 1] > 0:
        cnt += 1
    res += max(prices[i] - prices[i - 1], 0)

print(res, 2 * cnt)
