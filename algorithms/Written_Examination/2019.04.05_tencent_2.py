def solve(ch):

    return max(ch.count('0') - ch.count("1"), ch.count('1') - ch.count("0"))


import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline())
    ch = sys.stdin.readline()
    print(solve(ch))
