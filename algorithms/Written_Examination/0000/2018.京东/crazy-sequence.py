'''
假设第n项为k，从1加到k的值是sum=(k-1)*k//2，这个数可能大于或者等于n
如果n小于sum，那么解方程x^2+x-2n=0，x的值就会在k-和k之间，向上取整就是k了。

'''
import math
if __name__ == '__main__':
    x = int(input())
    a = (-1 + math.sqrt(1 + 8 * x)) / 2
    y = math.ceil(a)
    print(y)
