from collections import deque
n, m= map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a,b):
    que = deque()
    que.append((a,b))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if lst[nx][ny] == 1:
                lst[nx][ny] = lst[x][y] + 1
                que.append((nx,ny))


bfs(0,0)
print(lst[-1][-1])