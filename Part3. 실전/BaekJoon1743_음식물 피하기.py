from collections import deque

n, m, k = map(int, input().split())

lst = [[0 for _ in range(m)] for i in range(n)]

for i in range(k):
    r, c = map(int,input().split())
    lst[r-1][c-1] = 1

dx = [0,0,-1,1]
dy = [1,-1,0,0]

maxi = 1
def bfs(a,b):
    global maxi
    que = deque()
    que.append((a,b))
    cnt = 0
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if lst[nx][ny] == 1:
                lst[nx][ny] = lst[x][y] + 1
                cnt += 1
                que.append((nx,ny))
                maxi = max(maxi, cnt)

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            bfs(i,j)
print(maxi)