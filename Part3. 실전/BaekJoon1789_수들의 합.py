# 최대값은 작은거만더했을때 200이 되는 거

# 200
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19


def sum_lst(n):
    return int((n*(1+n))/2)

S = int(input())


if S == 1:
    print(1)
elif S == 2:
    print(1)
else:
    idx = 2
    while True:
        # 마지막 인덱스 값보다 작게 남았을때
        if idx >= S - sum_lst(idx):
            print(idx)
            break
        idx = idx + 1


