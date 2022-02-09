
n, k = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i] == lst[j]:
            lst[i] = [lst[i],j]
            break
    else:
        lst[i] = [lst[i],999]

lst[-1] = [lst[-1],999]

tap = []
check = set()
cnt = 0
for i in range(len(lst)):

    if lst[i][0] in check:
        # 안에 있는경우a
        for k in range(len(tap)):
            if tap[k][0] == lst[i][0]:
                tap[k][1] = lst[i][1]
                break
        continue
    else:
        # 안에 없는경우
        if len(tap) >= n:
            tap.sort(key=lambda x:x[1])
            (a,b) = tap.pop()
            check.remove(a)
            cnt += 1
        tap.append(lst[i])
        check.add(lst[i][0])

print(cnt)
