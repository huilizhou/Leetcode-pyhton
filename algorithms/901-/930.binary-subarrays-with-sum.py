class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        # 人家的解法
        # num, a, B = 0, len(A), [-1]
        # for i in range(0, a):
        #     if A[i]:
        #         B.append(i)
        # B.append(a)
        # b = len(B)
        # if b < S:
        #     return 0
        # elif S:
        #     for i in range(0, b - S - 1):
        #         num += (B[i + 1] - B[i]) * (B[S + i + 1] - B[S + i])
        # else:
        #     for i in range(0, b - S - 1):
        #         num += (B[i + 1] - B[i]) * (B[i + 1] - B[i] - 1) // 2
        # return num

        lenA = len(A)
        l = [-1]
        count = 0

        if not lenA:
            return 0

        for i in range(lenA):
            if A[i] == 1:
                l.append(i)

        l.append(lenA)
        lenL = len(l)

        if not S:
            i == 0
            while i + 1 < lenL:
                x = l[i + 1] - l[i] - 1
                count += (1 + x) * x // 2
                i += 1
        else:
            a = 0
            b = S
            while b < lenL - 1:
                count += (l[a + 1] - l[a]) * (l[b + 1] - l[b])
                b += 1
                a += 1
        return int(count)


print(Solution().numSubarraysWithSum(A=[1, 0, 1, 0, 1], S=2))
