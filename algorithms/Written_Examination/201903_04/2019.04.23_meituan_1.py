# # 通过27%
# '''
# 我的解法
# '''
# if __name__ == "__main__":
#     n = int(input())
#     A = [int(i) for i in input().strip().split()]
#     for i in A:
#         print(4 * i + 1)


# 人家的写法，优化需要规律，100%
a = int(input())
N = list(map(int, input().spilt()))
for n in N:
    if n % 2 == 0:
        print(4 * n + 1)
    elif n % 4 == 1:
        print(3 + int(n // 4) * 8)
    else:
        print(n + 1)
