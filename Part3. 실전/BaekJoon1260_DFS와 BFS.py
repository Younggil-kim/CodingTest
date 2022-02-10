from collections import deque

n,m,v = map(int, input().split())
lst = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in range(1, n+1):
    lst[i].sort()

lst_dfs = []
lst_bfs = []
def dfs(n):
    lst_dfs.append(n)
    visited[n] = True
    for i in lst[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    visited[n] = True
    que = deque([n])
    while que:
        x = que.popleft()
        lst_bfs.append(x)
        for i in lst[x]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


dfs(v)
visited = [False for _ in range(n+1)]
bfs(v)

print(*lst_dfs)
print(*lst_bfs)