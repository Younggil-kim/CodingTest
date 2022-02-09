

n, s = map(int, input().split())

lst = list(map(int, input().split()))

first = 0
second = 0
mini = 100001
result = 0
while True:
    # 머리가 끝에 도달하지 않았을때
    if result >= s:
        # 값보다 큰 경우 꼬리를 당겨온다
        mini = min(mini, second - first)
        result = result - lst[first]
        first = first + 1
    elif second == n:
        break
    else:
        # 값보다 작은경우 머리를 늘린다
        result = result + lst[second]
        second = second + 1

if mini == 100001:
    print(0)
else:
    print(mini)