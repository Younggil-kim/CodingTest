

n, m = map(int, input().split())
sx,sy,d = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))


def rotate(cd):
    nd = 0
    if cd == 0:
        # d가 북이면 nd는 서
        nd = 3
    elif cd == 1:
        # d가 동이면 nd는 북
        nd = 0
    elif cd == 2:
        # d가 남이면 nd는 동
        nd = 1
    elif cd == 3:
        # d가 서면 nd는 남
        nd = 2
    return nd


# d = 0 북 d == 1 동 , 2남, 3서

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def back(d):
    if d == 0:
        nd = 2
    elif d == 1:
        nd = 3
    elif d == 2:
        nd = 0
    elif d == 3:
        nd = 1
    return nd


end = False
while True:
#     1. 현재위치를 청소한다
    lst[sx][sy] = 2
#     2. 현재 위치에서 현재 방향 기준으로 왼쪽부터 인접 간 탐색
    chk = [True, True, True, True]
    while True:
        nd = rotate(d)
        nx = sx + dx[nd]
        ny = sy + dy[nd]
        if lst[nx][ny] == 0:
            # 청소를 아직 안한곳인경우
            sx = nx
            sy = ny
            d = nd
            break
        elif lst[nx][ny] == 1 or lst[nx][ny] == 2:
            chk[nd] = False
            d = nd
        if chk.count(False) == 4:
#             4방향 다 못가는 경우 한칸 후진
            back_d = back(nd)
            bx = sx + dx[back_d]
            by = sy + dy[back_d]
            if lst[bx][by] == 1:
                end = True
                break
            else:
                sx = bx
                sy = by
                break
    if end:
        break

cnt = 0
for i in range(len(lst)):
    cnt += lst[i].count(2)
print(cnt)