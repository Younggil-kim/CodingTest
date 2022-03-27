from collections import deque

n, m = map(int ,input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def melt():
    global lst
    copy = [item[:] for item in lst]
    for i in range(n):
        for j in range(m):
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if lst[nx][ny] == 0:
                    cnt += 1
            copy[i][j] -= cnt
            if copy[i][j] < 0:
                copy[i][j] = 0
    lst = [item[:] for item in copy]

def bfs(a,b):
    global copys
    qu = deque()
    qu.append((a,b))
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if copys[nx][ny] != 0:
                qu.append((nx,ny))
                copys[nx][ny] = 0
    return True

cnt = 0
chk_lst = [[0 for _ in range(m)] for k in range(n) ]

while True:

    chk = 0
    cnt = cnt + 1
    melt()
    copys = [item[:] for item in lst]
    if chk_lst == lst:
        print(0)
        break
    for i in range(n):
        for j in range(m):
            if copys[i][j] != 0:
                bfs(i, j)
                chk += 1
    if chk >= 2:
        print(cnt)
        break

