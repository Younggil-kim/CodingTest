# 시간, 메모리 초과
# from itertools import combinations
#
# n, k = map(int, input().split())
# #anta tica = a n t i c 5개로 이루어짐
# #몇개의 종류가 아니라 어떻게 이루어져있나가 중요한데
# #일단 종류 세서 k개 넘기면 out
# lst = []
# grp = []
#
# for i in range(n):
#     tmp = input()
#     tmp = tmp[4:-4]
#     tmp = list(set(tmp))
#     grp = grp + tmp
#     lst.append(tmp)
#
# if k < 5:
#     print(0)
# else:
#     k = k - 5
#     grp = list(set(grp))
#     # words = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm','o', 'p', 'q', 'r', 's',  'u', 'v', 'w', 'x', 'y', 'z']
#     candi = combinations(grp, k)
#
#     maxi = -100
#     for can in candi:
#         cnt = 0
#         for i in range(len(lst)):
#             for k in lst[i]:
#                if k not in can:
#                    if k in "anict":
#                     continue
#                    else:
#                     break
#             else:
#                 cnt = cnt + 1
#                 if cnt == 8:
#                     print(can)
#         maxi = max(cnt, maxi)
#     print(maxi)

import sys
n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

ans = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26

for c in ('a','c','i','n','t'):
    learn[ord(c) - ord('a')] = 1

def dfs( idx , cnt):
    global ans

    if cnt == k - 5:
        rCnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w)- ord('a')]:
                    check = False
                    break
            if check:
                rCnt += 1
        ans = max(ans, rCnt)
        return

    for i in range(idx,26):
        if not learn[i]:
            learn[i] = 1
            dfs(i, cnt+1)
            learn[i] = 0

dfs(0,0)
print(ans)
