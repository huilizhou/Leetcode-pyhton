import sys


def solver(num1, num2):
    num1.sort()
    num2.sort()
    if num1[0] >= 0 and num2[-1] <= 0:
        return num1[1] * num2[-1]
    elif num1[-1] <= 0 and num2[0] >= 0:
        return num1[-2] * num2[0]
    else:
        min_1 = num1[0] * num2[0]
        max_1 = num1[-1] * num2[-1]
        if max_1 > min_1:
            return max(num1[-2] * num2[-1], min_1)
        else:
            return max(max_1, num1[1] * num2[0])


if __name__ == "__main__":

    line1 = sys.stdin.readline().strip()
    m, n = list(map(int, line1.split()))
    line2 = sys.stdin.readline().strip()
    valuesA = list(map(int, line2.split()))
    line3 = sys.stdin.readline().strip()
    valuesB = list(map(int, line3.split()))

    # valuesA = [-1, 0, 1, 2, 3]
    # valuesB = [-1, 0, 1]
    print(solver(valuesA, valuesB))
