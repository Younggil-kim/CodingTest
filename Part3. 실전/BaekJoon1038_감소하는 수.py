

from itertools import combinations

n = int(input())
lst = ['1','2','3','4','5','6','7','8','9','0']
result = []
for i in range(1,11):
    nums = list(combinations(lst, i))
    for num in nums:
        num = list(num)
        num.sort(reverse=True)
        tmp = int(''.join(num))
        result.append(tmp)
result.sort()
if n >= len(result):
    print(-1)
else:
    print(result[n])


# 잘못 푼 코드
# 10
# 20 21
# 30 31 32
# def check(num):
#     lst = list(str(num))
#
#     if len(lst) != len(set(lst)):
#         return False
#     else:
#         lst.sort(reverse=True)
#         tmp = int(''.join(lst))
#
#         if tmp == num:
#             return True
#         else:
#             return False
# result = []
# for i in range(9876543212):
#     if check(i):
#         result.append(i)
# print(result)
# if len(result) < n:
#     print(-1)
# else:
#     print(result[n])