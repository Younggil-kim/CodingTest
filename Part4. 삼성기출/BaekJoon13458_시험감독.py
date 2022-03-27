import math
n = int(input())
lst = list(map(int, input().split()))
b, c = map(int, input().split())


# b는 총감독관이 관리할 응시자 수
# c는 부감독관이 한 시험장에서 감시할 수
# b는 한명만 있을 수 있고 부감독관은 여러명 있어야함
result = 0
for i in lst:
    total = i - b
    if total <= 0:
        result += 1
    else:
        sub = math.ceil(total/c)
        result += sub+1
print(result)