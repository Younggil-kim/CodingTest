import sys
input = sys.stdin.readline

lst = [0 for _ in range(1001)]
lst[1] = 1
for i in range(2,1001):
    n = 2
    if lst[i] == 1:
        continue
    while True:
        if n*i >= 1001:
            break
        lst[n*i] = 1
        n = n + 1

n = int(input())
nums = map(int,input().split())

cnt = 0
for i in nums:
    if lst[i] == 0:
        cnt = cnt + 1
print(cnt)