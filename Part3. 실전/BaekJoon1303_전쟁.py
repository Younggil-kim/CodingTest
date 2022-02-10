from collections import deque

n, m = map(int, input().split())

lst = []
for i in range(m):
    lst.append(list(input()))

sumW = 0
sumB = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b,c):
    global sumW
    global sumB
    que = deque()
    que.append((a,b))
    cnt = 0
    while que:
        x , y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or ny >= n or nx < 0 or ny < 0:
                continue
            if lst[nx][ny] == c:
                cnt += 1
                lst[nx][ny] = 'P'
                que.append((nx,ny))
    if c == 'W':
        if cnt == 0:
            sumW += 1
        else:
            sumW += cnt**2
    elif c == 'B':
        if cnt == 0:
            sumB += 1
        else:
            sumB += cnt**2

for i in range(m):
    for j in range(n):
        if lst[i][j] == 'W':
            bfs(i,j,'W')
        elif lst[i][j] == 'B':
            bfs(i,j,'B')

print(sumW, sumB)