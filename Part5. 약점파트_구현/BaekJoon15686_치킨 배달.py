# 골드 5 30분
from itertools import combinations

n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))

# 거리 체크 함수
def cal_bbq(hx,hy, bx,by):

    return abs(hx-bx) + abs(hy-by)

home = []
bbq = []

# 좌표 받아오기
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            home.append((i,j))
        elif lst[i][j] == 2:
            bbq.append((i,j))


comb = [i for i in range(len(bbq))]

distance = []

last = 9999

grp = list(combinations( comb,m))
mini = 9999
while grp:
    candi = grp.pop()
    total = 0
    for k in range(len(home)):
        # 각 집의 최소값구하기
        home_mini = 9999
        for l in candi:
            bbx, bby = bbq[l]
            home_mini = min(home_mini,cal_bbq(bbx,bby, home[k][0],home[k][1]))
        #    위 반복문이 끝나면 한 집의 치킨거리가 나옴
        total += home_mini
        # cnt는 각 집 전체의 치킨거리
    mini = min(mini,total)
print(mini)
