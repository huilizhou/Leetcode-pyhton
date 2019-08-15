class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # 人家的解法
        # import heapq
        # heap, res, idx, ugly_by_last_prime = [], [
        #     0] * n, [0] * len(primes), [0] * n
        # res[0] = 1
        # for index, val in enumerate(primes):
        #     heapq.heappush(heap, (val, index))
        # for i in range(1, n):
        #     res[i], k = heapq.heappop(heap)
        #     ugly_by_last_prime[i] = k
        #     idx[k] += 1
        #     while ugly_by_last_prime[idx[k]] > k:
        #         idx[k] += 1
        #     heapq.heappush(heap, (primes[k] * res[idx[k]], k))
        # return res[-1]

        inx = [0 for i in primes]
        res = [1]
        for _ in range(1, n):
            res.append(min([res[inx[j]] * primes[j] for j in range(len(inx))]))
            for j in range(len(inx)):
                if res[-1] == res[inx[j]] * primes[j]:
                    inx[j] += 1
        return res[-1]


print(Solution().nthSuperUglyNumber(n=12, primes=[2, 7, 13, 19]))
