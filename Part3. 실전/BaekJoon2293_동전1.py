

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

dp = [0 for _ in range(k+1)]
# 0 0 0 000 0
dp[0] = 1
#  1 2 5
#          0 1 2 3 4 5 6 7 8 9 10
#          1         1         1
#              1 1
#1을 봤을때 1 1 1 1 1 1 1 1 1 1 1
#2를 봤을때     2 2 3 3 4 4 5 5 6
#5를 봤을때           4 5 6 7 8 10
# [3-2]가 값이 있으면
# [3]에 [3-2]를 더해준다
for coin in coins:
    for idx in range(coin, k+1):
        if dp[idx- coin] != 0:
            dp[idx] = dp[idx] + dp[idx-coin]

print(dp[-1])