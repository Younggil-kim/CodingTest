# 한 행, 열에 연속된 같은 색이 몇개 들어가있는지 들어간 함수 제작


n = int(input())
lst = []
for _ in range(n):
    a = list(input())
    lst.append(a)


def finder(n):
    # 가로
    maxi = 0
    for i in range(n):
        stack = []
        for j in range(n):
            if len(stack) == 0:
                stack.append(lst[i][j])
                maxi = max(maxi, len(stack))
            else:
                # 같은경우
                if stack[-1] == lst[i][j]:
                    stack.append(lst[i][j])
                    maxi = max(maxi, len(stack))
                else:
                    stack.clear()
                    stack.append(lst[i][j])
                    maxi = max(maxi, len(stack))

    #세로
    for i in range(n):
        stack = []
        for j in range(n):
            if len(stack) == 0:
                stack.append(lst[j][i])
                maxi = max(maxi, len(stack))
            else:
                # 같은경우
                if stack[-1] == lst[j][i]:
                    stack.append(lst[j][i])
                    maxi = max(maxi, len(stack))
                else:
                    stack.clear()
                    stack.append(lst[j][i])
                    maxi = max(maxi, len(stack))
    return maxi

dx = [0,0,1,-1]
dy = [1,-1,0,0]
maxi = 0
for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= n or ny >= n or nx < 0 or nx < 0:
                continue
            lst[i][j], lst[nx][ny] = lst[nx][ny], lst[i][j]
            maxi = max(maxi, finder(n))
            lst[nx][ny], lst[i][j] = lst[i][j], lst[nx][ny]
print(maxi)