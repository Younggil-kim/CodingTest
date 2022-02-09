

a,b = map(int, input().split())
lst = list(map(int, input().split()))


maxi = -1
cnt = 0

before = sum(lst)

#리스트 순환하면서
#양옆에가 자기보다 크면 올리기 + 1
def left(idx):
    for i in range(idx,-1,-1):
        if lst[i] > lst[idx]:
            return True
    return False

def right(idx):
    for i in range(idx,len(lst)):
        if lst[i] > lst[idx]:
            return True
    return False

for i in range(1,b-1):
    while left(i) and right(i):
        lst[i] += 1


print(sum(lst)-before)