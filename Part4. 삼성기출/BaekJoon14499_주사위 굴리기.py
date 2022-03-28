n,m, x,y, k = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

cmd = []
cmd.append(list(map(int,input().split())))

print(lst,cmd)

dice = [0,0,0,0,0,0,0]

def convert(num):
    if num == 1:
        return 6
    elif num == 2:
        return 5
    elif num == 3:
        return 4
    elif num == 4:
        return 3
    elif num == 5:
        return 2
    elif num == 6:
        return 1

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
        dice[3] = d2
        dice[2] = d1
    elif cm == 4:
        dice[1] = d2
        dice[5] = d1
        dice[6] = d5
        dice[2] = d6
# 1동 2서 3북 4남


dx = [0,0,-1,1]
dy = [1,-1,0,0]
