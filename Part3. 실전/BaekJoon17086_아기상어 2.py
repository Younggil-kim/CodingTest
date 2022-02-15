from collections import deque

n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

dx = [-1, -1, -1, 0,  0, 1, 1, 1]
dy = [ 0,  1, -1, 1, -1, 0, 1, -1]


maxi = 0

def bfs(a,b):
    que = deque()
    que.append((a,b))
    cnt = 0
    check = [item[:] for item in lst]
    while que:
        x, y = que.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if check[nx][ny] == 0:
                check[nx][ny] = check[x][y] + 1
                que.append((nx,ny))
            elif lst[nx][ny] == 1:
                check[nx][ny] = check[x][y] + 1
                return check[nx][ny]
    return cnt

for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            maxi = max(bfs(i,j), maxi)
print(maxi)