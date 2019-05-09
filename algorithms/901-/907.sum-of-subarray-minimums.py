# zishuzu
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = [0] + A
        # result[i]是所有以A[i]为结束的子序列的结果
        # 比如result[2]=min([3,1,2])+min([1,2])+min([2])
        result = [0] * len(A)
        stack = [0]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop()
            # A[j]是序列中第一个小于A[i]的值
            # 在不包含A[j]的子序列A[j+1:i+1],A[j+2:i+1]...中，最小值为A[i]
            # 因此result[i]=result[j]+(i-j)*A[i]
            j = stack[-1]
            result[i] = result[j] + (i - j) * A[i]
            stack.append(i)
        return sum(result) % (10**9 + 7)


print(Solution().sumSubarrayMins([3, 1, 2, 4]))
