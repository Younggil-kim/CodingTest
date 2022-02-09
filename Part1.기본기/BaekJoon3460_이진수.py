import sys
input = sys.stdin.readline

n = int(input())

def printBin(num):
    lst = []
    num = num[2:]
    num = list(num)
    num.reverse()
    for i in range(len(num)):
        if num[i] == "1":
            lst.append(i)
    print(*lst)


for _ in range(n):
    a = int(input())
    printBin(bin(a))#13 > 0b


