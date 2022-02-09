import sys
input = sys.stdin.readline


maxi = 0
cur = 0
for i in range(10):
    inpt, outpt = map(int, input().split())
    cur = cur - inpt
    cur = cur + outpt
    maxi = max(maxi, cur)
print(maxi)