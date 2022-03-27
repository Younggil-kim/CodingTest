
answer = -1
# board = ["11111","11111","11111","11111","11111"]
# h = 5
# w = 5
# n = 5

board = ["111100000","000010011","111100011","111110011","111100011","111100010","111100000"]
h = 7
w = 9
n = 4
def first(i, j, n):  # 가로

    for k in range(n):
        if j + k >= w:
            return False
        else:
            if board[i][j + k] == '0':
                return False
    if j == 0:
        if j + n == w:
            return True
        if board[i][j + n] == '1':
            return False
    elif j + n == w:
        if board[i][j - 1] == '1':
            return False
    else:
        if board[i][j - 1] == '1' or board[i][j + n] == '1':
            return False
    return True

def second(i, j, n):  # 세로

    for k in range(n):
        if i + k >= h:
            return False
        else:
            if board[i+k][j] == '0':
                return False
    if i == 0:
        if i + n == h:
            return True
        if board[i+n][j] == '1':
            return False
    elif i + n == h:
        if board[i-1][j] == '1':
            return False
    else:
        if board[i-1][j] == '1' or board[i+n][j] == '1':
            return False
    return True

def third(i, j, n):  # 아래대각선

    for k in range(n):
        if i + k >= h or j + k >= w:
            return False
        else:
            if board[i+k][j+k] == '0':
                return False

    if i == 0 or j == 0:
        if i + n == h and j + n == w:
            return True
        if i + n < h and j + n >= w:
            return True
        if i + n >= h and j + n < w:
            return True
        if board[i+n][j+n] == '1':
            return False
    elif i + n == h or j + n == w:
        if board[i-1][j-1] == '1':
            return False
    else:
        if board[i-1][j-1] == '1' or board[i+n][j+n] == '1':
            return False
    return True


def fourth(i, j, n):  # 윗대각선

    for k in range(n):
        if i -k < 0 or j + k >= w:
            return False
        else:
            if board[i-k][j+k] == '0':
                return False

    if i == h-1 or j == 0:
        if i - n == -1 and j + n == w:
            return True
        if i -n  > -1 and j + n >= w:
            return True
        if i - n <= -1 and j + n < w:
            return True
        if board[i-n][j+n] == '1':
            return False
    elif i - n == 0 or j + n == w:
        if board[i+1][j-1] == '1':
            return False
    else:
        if board[i-1][j-1] == '1' or board[i-n][j+n] == '1':
            return False
    return True

for a in range(h):
    for b in range(w):
        if first(a,b,n):
            answer += 1
            print("first",a,b)
        if second(a,b,n):
            answer += 1
            print("second",a,b)
        if third(a,b,n):
            answer += 1
            print("third",a,b)
        if fourth(a,b,n):
            answer += 1
            print("fourth",a,b)
print(first(0,0,5))