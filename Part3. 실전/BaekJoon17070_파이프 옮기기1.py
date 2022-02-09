from collections import deque

# def dfs(a,b,dir):
#     global result
#     if a == n-1 and b == n-1:
#         result.append(1)
#         return
#     # 가로인경우
#     if dir == 0:
#         if b + dy[0] < n:
#             if lst[a + dx[0]][b + dy[0]] != 1:
#                 dfs(a+dx[0], b+ dy[0], 0)
#         if a + dx[2] < n and b + dy[2] < n:
#             if lst[a + dx[2]][b + dy[2]] != 1 and lst[a + dx[0]][b + dy[0]] != 1 and lst[a + dx[1]][b + dy[1]] != 1:
#                 dfs(a+dx[2], b+ dy[2], 2)
#     # 세로인경우
#     elif dir == 1:
#         if a + dx[1] < n:
#             if lst[a + dx[1]][b + dy[1]] != 1:
#                 dfs(a+dx[1], b+ dy[1], 1)
#         if a + dx[2] < n and b + dy[2] < n:
#             if lst[a + dx[2]][b + dy[2]] != 1 and lst[a + dx[0]][b + dy[0]] != 1 and lst[a + dx[1]][b + dy[1]] != 1:
#                 dfs(a+dx[2], b+ dy[2], 2)
#     # 대각선인경우
#     elif dir == 2:
#         if b + dy[0] < n:
#             if lst[a + dx[0]][b + dy[0]] != 1:
#                 dfs(a+dx[0], b+ dy[0], 0)
#         if a + dx[1] < n:
#             if lst[a + dx[1]][b + dy[1]] != 1:
#                 dfs(a+dx[1], b+ dy[1], 1)
#         if a + dx[2] < n and b + dy[2] < n:
#             if lst[a + dx[2]][b + dy[2]] != 1 and lst[a + dx[0]][b + dy[0]] != 1 and lst[a + dx[1]][b + dy[1]] != 1:
#                 dfs(a+dx[2], b+ dy[2], 2)


n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

# 오, 아, 대
dx = [0, 1, 1]
dy = [1, 0, 1]


result = 0
def dfs(a,b,dir):
    global result
    if a == n-1 and b == n-1:
        result += 1
        return
    if dir == 0 or dir == 2:
        if b +1 < n:
            if lst[a][b+1] == 0:
                dfs(a,b+1,0)
    if dir == 1 or dir == 2:
        if a + 1 < n:
            if lst[a+1][b] == 0:
                dfs(a+1,b,1)
    if dir == 0 or dir == 1 or dir == 2:
        if b +1 < n and a+1 < n:
            if lst[a][b+1] == 0 and lst[a+1][b] == 0and lst[a+1][b+1] == 0:
                dfs(a+1,b+1,2)

dfs(0,1,0)
print(result)

