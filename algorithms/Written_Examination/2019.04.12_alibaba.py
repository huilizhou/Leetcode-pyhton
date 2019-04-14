class Sloution:
    def test(self, M, N, K):
        if M == 1 and N == 1 and K >= 2:
            return 1


import sys
if __name__ == "__main__":
    M = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())
    print(Sloution().test(M, N, K))
