from itertools import combinations
import sys
input = sys.stdin.readline

# 첫번째 방식
# lst = []
# for i in range(9):
#     lst.append(int(input()))
#
# result = list(combinations(lst,7))
#
# for items in result:
#     if (sum(items)) == 100:
#         last = list(items)
#         break
# last.sort()
# for i in last:
#     print(i)

lst = []
for i in range(9):
    lst.append(int(input()))

lstSum = sum(lst)
diff = lstSum - 100

flag= False
for i in range(8):
    a = lst[i]
    for j in range(i+1,9):
        # print(j)
        b = lst[j]
        if a + b == diff:
            lst.remove(a)
            lst.remove(b)
            flag = True
            break
    if flag:
        break
lst.sort()
for item in lst:
    print(item)

