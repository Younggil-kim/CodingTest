# 오른쪽 이동시 오른쪽부터 합쳐짐
# dfs 5번
from itertools import product

n = int(input())
lst = []
for i in range(n):

    lst.append(list(map(int, input().split())))

# print(lst)

def rotate_matrix_90_degree():
    global lst
    row = len(lst)
    col = len(lst[0])

    res = [[0] * row for _ in range(col)]
    for r in range(row):
        for c in range(col):
            res[c][row-1-r] = lst[r][c]
    lst = res

def rotate_reverse():
    global lst
    lst =  list(map(list, zip(*lst)))[::-1]

# print()

def left():
    global lst
    for i in range(n):
        if 0 in lst[i]:
            cnt = 0
            while 0 in lst[i]:
                lst[i].remove(0)
                cnt += 1
            for u in range(cnt):
                lst[i].append(0)
        chk = [False for _ in range(n)]
        for j in range(0,n-1):
            k = j + 1


            if lst[i][j] == lst[i][k] and chk[j] is False and chk[k] is False:
                lst[i][j] += lst[i][k]
                lst[i][k] = 0
                chk[j] = True
                chk[k] = True
        if 0 in lst[i]:
            cnt = 0
            while 0 in lst[i]:
                lst[i].remove(0)
                cnt += 1
            for u in range(cnt):
                lst[i].append(0)
    # print("left")
    return

def right():
    rotate_matrix_90_degree()
    rotate_matrix_90_degree()
    left()
    rotate_reverse()
    rotate_reverse()
    # print("right")
    return

def up():
    rotate_matrix_90_degree()
    rotate_matrix_90_degree()
    rotate_matrix_90_degree()
    left()
    rotate_reverse()
    rotate_reverse()
    rotate_reverse()
    # print("up")
    return

def down():
    rotate_matrix_90_degree()
    left()
    rotate_reverse()
    # print("down")
    return



result = []
cmd = [0,1,2,3]
cmds = list(product(cmd,repeat=5))

copys = [item[:] for item in lst]
for cmd in cmds:
    lst = [item[:] for item in copys]
    for a in cmd:
        if a == 0:
            left()
        elif a == 1:
            up()
        elif a == 2:
            down()
        elif a == 3:
            right()
    result.append(max(map(max,lst)))

print(max(result))
