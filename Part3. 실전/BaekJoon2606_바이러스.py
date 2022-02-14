from collections import deque

n = int(input())

m = int(input())

lst = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in range(1, n+1):
    lst[i].sort()

lst_dfs = []
def dfs(n):
    lst_dfs.append(n)
    visited[n] = True
    for i in lst[n]:
        if not visited[i]:
            dfs(i)



dfs(1)

print(len(lst_dfs)-1)