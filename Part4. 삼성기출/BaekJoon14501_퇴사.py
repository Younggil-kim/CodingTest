

n = int(input())
T = []
P = []

for i in range(n):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

dp = [0 for _ in range( n+2)]

tmp = 0
for i in range(1,n+1):
    tmp = max(dp[i] ,tmp)
    if i + T[i-1] > n+1:
        continue
    dp[i+T[i-1]] = max(dp[i+T[i-1]], P[i-1]+ tmp)
print(dp)