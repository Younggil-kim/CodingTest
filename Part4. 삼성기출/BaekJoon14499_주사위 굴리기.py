
n,m, x,y, k = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

cmds = list(map(int,input().split()))

dice = [0,0,0,0,0,0,0]

def command(cm):
    global dice
    d1,d2,d3,d4,d5,d6 = dice[1:]
    if cm == 1:
        dice[1] = d4
        dice[4] = d6
        dice[6] = d3
        dice[3] = d1
    elif cm ==2:
        dice[1] = d3
        dice[4] = d1
        dice[3] = d6
        dice[6] = d4
    elif cm == 3:
        dice[1] = d5
        dice[5] = d6
        dice[6] = d2
        dice[2] = d1
    elif cm == 4:
        dice[1] = d2
        dice[5] = d1
        dice[6] = d5
        dice[2] = d6
# 1동 2서 3북 4남


dx = [0,0,-1,1]
dy = [1,-1,0,0]

for cmd in cmds:
    nx = x + dx[cmd-1]
    ny = y + dy[cmd-1]
    if nx < 0 or ny < 0 or nx >= n  or ny >= m:
        continue
    if lst[nx][ny] == 0:
    # 0인경우
        command(cmd)
        lst[nx][ny] = dice[6]
        print(dice[1])
    else:
        # 0이 아닌경우
        command(cmd)
        dice[6] = lst[nx][ny]
        lst[nx][ny] = 0
        print(dice[1])
    x = nx
    y = ny

