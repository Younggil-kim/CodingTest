from collections import deque

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int,input())))


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(a,b):
    qu = deque()
    qu.append((a,b))
    maxi = 0
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if lst[nx][ny] == 1:
                lst[nx][ny] = lst[x][y] + 1
                qu.append((nx,ny))
                maxi += 1
    return maxi

result = []

for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            cnt = bfs(i,j)
            if cnt == 0:
                result.append(1)
            else:
                result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)

