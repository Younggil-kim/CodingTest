

n, k = map(int, input().split())


lst = [10001 for _ in range(k + 1)]

coins= []
lst[0] = 0
for i in range(n):
    coins.append(int(input()))

for i in range(len(lst)):
    for coin in coins:
        if i - coin < 0:
            continue
        if lst[i-coin] != 10001:
            lst[i] = min(lst[i], lst[i-coin]+1)

if lst[-1] == 10001:
    print(-1)
else:
    print(lst[-1])
