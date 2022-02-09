import sys
input = sys.stdin.readline

lst = [0 for _ in range(10001)]
lst[1] = 1
for i in range(2,10001):
    n = 2
    if lst[i] == 1:
        continue
    while True:
        if n*i >= 10001:
            break
        lst[n*i] = 1
        n = n + 1

start = int(input())
end = int(input())

result = []
for i in range(start,end+1):
    if( lst[i] == 0 ):
        result.append(i)

if(len(result) == 0):
    print(-1)
else:
    print(sum(result))
    print(result[0])