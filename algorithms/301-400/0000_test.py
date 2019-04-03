# s = "loveleetcode"
# print(s.find("l"), s.rfind("l"))
# mask = 0
# mask |= 1 << (ord("c") - 97)
# print(mask)
# print(1 << (ord("c") - 97))
# print(0 | 1)
# print(~60)
amount = 11
coins = [1, 2, 5]
dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]
print(dp)
