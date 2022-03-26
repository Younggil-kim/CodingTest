#이것도 왼쪽으로만 빼고 넣고 하면 될듯?
from itertools import product
import sys
from collections import deque
from itertools import permutations
n, m = map(int, input().split())
grp = []
for i in range(n):

    grp.append(list(input()))


def rotate_90(grp0):
    grp0 = list(map(list, zip(*grp0[::-1])))
    return grp0
def rotate_reverse(grp0):

    grp0 = list(map(list, zip(*grp0)))[::-1]
    return grp0

def left(lst):
    # 전 라인을 돌면서 왼쪽으로 보내기
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == 'R':
                # 굴러 갈 수 있는 경우
                if lst[i][j-1] == '.':
                # 굴러 갈 수 없는 경우

                    start = j - 1
                    while True:
                        if lst[i][start] == 'O':
                            lst[i][j] = '.'
                            result.append("R")
                            break
                        if lst[i][start] != '.':
                            lst[i][start+1], lst[i][j] = lst[i][j], lst[i][start+1]
                            break
                        start -= 1
                elif lst[i][j-1] == 'O':
                    lst[i][j] = '.'
                    result.append("R")

            elif lst[i][j] == 'B':
                # 굴러 갈 수 있는 경우
                if lst[i][j - 1] == '.':
                    # 굴러 갈 수 없는 경우

                    start = j - 1
                    while True:
                        if lst[i][start] == 'O':
                            lst[i][j] = '.'
                            result.append("B")
                            break
                        if lst[i][start] != '.':
                            lst[i][start + 1], lst[i][j] = lst[i][j], lst[i][start + 1]
                            break
                        start -= 1
                elif lst[i][j - 1] == 'O':
                    lst[i][j] = '.'
                    result.append("B")


    return lst, result

def down(lst):
    lst = rotate_90(lst)
    a, res = left(lst)
    a = rotate_reverse(a)
    return a, res
def right(lst):
    lst = rotate_90(lst)
    lst = rotate_90(lst)
    a, res = left(lst)
    a = rotate_reverse(a)
    a = rotate_reverse(a)
    return a, res
def up(lst):
    lst= rotate_reverse(lst)
    a ,res = left(lst)
    a = rotate_90(a)
    return a, res


def bfs(n,cmd,value):
    qu = deque()
    qu.append((n,cmd,value))
    while qu:
        num,cm, vals = qu.popleft()

        if num == 10:
            print(-1)
            break

        if cm == -1:
            val = [item[:] for item in vals]
            a, res = left(val)
            if len(res) == 1 and res[0] == 'R':
                print(num+1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num+1,0, a))

            val = [item[:] for item in vals]
            b, res= right(val)
            if len(res) == 1 and res[0] == 'R':
                print(num+1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1,1, b))

            val = [item[:] for item in vals]
            c,res= down(val)
            if len(res) == 1 and res[0] == 'R':
                print(num+1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1,2, c))

            val = [item[:] for item in vals]
            d,res = up(val)
            if len(res) == 1 and res[0] == 'R':
                print(num+1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1,3, d))
        elif cm == 0:
            val = [item[:] for item in vals]
            b, res = right(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 1, b))

            val = [item[:] for item in vals]
            c, res = down(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 2, c))

            val = [item[:] for item in vals]
            d, res = up(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 3, d))
        elif cm == 1:
            val = [item[:] for item in vals]
            a, res = left(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 0, a))

            val = [item[:] for item in vals]
            c, res = down(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 2, c))

            val = [item[:] for item in vals]
            d, res = up(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 3, d))
        elif cm == 2:
            val = [item[:] for item in vals]
            a, res = left(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 0, a))

            val = [item[:] for item in vals]
            b, res = right(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 1, b))

            val = [item[:] for item in vals]
            d, res = up(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 3, d))
        elif cm == 3:
            val = [item[:] for item in vals]
            a, res = left(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 0, a))

            val = [item[:] for item in vals]
            b, res = right(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 1, b))

            val = [item[:] for item in vals]
            c, res = down(val)
            if len(res) == 1 and res[0] == 'R':
                print(num + 1)
                break
            elif len(res) == 1 and res[0] == 'B':
                pass
            elif len(res) == 2:
                pass
            elif len(res) == 0:
                qu.append((num + 1, 2, c))

bfs(0,-1,grp)
