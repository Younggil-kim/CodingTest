

def del1(num):
    num = str(num)[:-1]
    return int(num)

a,b = map(int, input().split())

cnt = 0
flag = False
while True:
    if a > b:
        flag = True
        break
    if a == b:
        break
    if str(b)[-1] == '1':
        b = del1(b)
        cnt += 1
    else:
        if b % 2 == 0:
            b = b // 2
            cnt += 1
        else:
            flag = True
            break
if flag:
    print(-1)
else:
    print(cnt+1)
