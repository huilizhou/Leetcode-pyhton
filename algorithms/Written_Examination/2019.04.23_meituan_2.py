# 通过36%
class solution:
    def solver(self, s, t):
        if len(s) < len(t):
            return 0
        res = 0
        k = 0
        for i in range(len(s) - len(t)):
            if s[i:i + len(t)] == t:
                res += 1
            else:
                for j in range(len(t)):
                    if s[j] != t[j] and s[j] != "?":
                        break
                    else:
                        k += 1
                if k == len(t):
                    res += 1
        return res


if __name__ == "__main__":
    # s = input()
    # t = input()
    s = 'AaAaAaA'
    t = 'aa'
    print(solution().solver(s, t))
