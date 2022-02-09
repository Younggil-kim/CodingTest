import sys
input = sys.stdin.readline

lst = []
i = 1
while True:
    for _ in range(i):
        lst.append(i)
    i = i + 1
    if(len(lst) >= 1001):
        break
a,b = map(int, input().split())
print(sum(lst[a-1:b]))
