from collections import deque

n, k = map(int, input().split())

if n == k:
    print(0)
    print(1)

else:
    que = deque()
    que.append((n-1, 1))
    que.append((n+1, 1))
    que.append((n*2, 1))
    count = 0
    time = 0
    mini = int(1e9)
    check = [False] * 100001
    check[n] = True
    while que:
        tmp, cnt = que.popleft()
        if tmp >= 100001 or tmp < 0:
            continue
        check[tmp] = True
        if tmp == k:
            mini = min(mini, cnt)
            if mini == cnt:
                count += 1
            continue
        if cnt > mini:
            break
        if tmp - 1 >= 0 and not check[tmp-1]:
            que.append((tmp - 1, cnt + 1))
        if tmp + 1 <= 100000 and not check[tmp+1]:
            que.append((tmp + 1, cnt + 1))
        if tmp*2 <= 100000 and not check[tmp*2]:
            que.append((tmp * 2, cnt + 1))
    print(mini)
    print(count)