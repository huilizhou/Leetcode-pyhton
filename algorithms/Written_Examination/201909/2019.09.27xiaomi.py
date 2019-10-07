import sys

if __name__ == "__main__":

    def permute(nums):
        # 递归法
        res = []
        if len(nums) <= 1:
            return [nums]
        for i in range(len(nums)):
            num = nums[i]
            newnums = nums[:i] + nums[i + 1:]
            for item in permute(newnums):
                res.append([num] + item)
        return res

    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))

    k = permute(values)
    for i in k:
        print(i)
