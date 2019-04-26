# # A = "this apple is sweet"
# # print(A.split())
# # B = "this apple is sour"
# # print((B.split() + A.split()))
# x = [1, 2, 3]
# # y = [4, 5, 6]
# # xy = zip(x, y)
# # print(xy)
# # x = zip(x)
# print(zip(x))

# # 求一组数的最大公约数


# def solver_gcd(nums):
#     smaller = min(nums)
#     for i in reversed(range(1, smaller + 1)):
#         if list(filter(lambda j: j % i != 0, nums)) == []:
#             return i


# print(solver_gcd([2, 4]))


# # 求一组数的最小公倍数
# def solver_lcm(nums):
#     greater = max(nums)
#     while True:
#         if list(filter(lambda i: greater % i != 0, nums)) == []:
#             return greater
#         greater += 1


# print(solver_lcm([2, 5, 10, 11]))
