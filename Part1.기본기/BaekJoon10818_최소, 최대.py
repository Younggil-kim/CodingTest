import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

result = []
result.append(min(lst))
result.append(max(lst))

print(*result)