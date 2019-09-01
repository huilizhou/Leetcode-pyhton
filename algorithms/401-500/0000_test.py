# s = "asdfghjkl"
# print(set(s))

# a = 23
# if a > 18:
#     print("adult")
# elif a >= 6:
#     print("tennager")
# else:
#     print("kid")

# a = ["a", "b", "c", "d", "e", "f", "g", "h"]
# b = a[:]
# print(a)
# print(b)
# print("ida=", id(a), "\n", id(b))
# a[:] = [101, 102, 103]
# print(a)
# print("ida=", id(a), "\n", id(b))


# nums = "sssaabcdd"
# import collections
# nums1 = collections.Counter(nums)
# for k, v in nums1.most_common():
#     print(k, v)
# print(nums1)


# dic = {'a': 1, 'b': 2, 'c': 1}
# for k, v in dic.items():
#     print(k, v)


L = [1, 2, 3, 5]
print(sum(L) % 2)
